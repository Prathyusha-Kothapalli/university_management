import uuid
from datetime import datetime
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Header, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.models.role import Role
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
    check_permission,
    ROLE_PERMISSIONS,
)
from app.services.auth_service import (
    validate_password_strength,
    log_auth_event,
    check_account_lockout,
    record_failed_login,
    clear_failed_login,
    generate_password_reset_token,
    verify_password_reset_token,
    consume_password_reset_token,
    generate_email_verification_token,
    verify_email_token,
    generate_totp_secret,
    verify_totp_code,
    generate_backup_codes,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class RegisterRequest(BaseModel):
    full_name: str
    email: str
    password: str
    role_name: str = "student"


class LoginRequest(BaseModel):
    email: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class ForgotPasswordRequest(BaseModel):
    email: str


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


class VerifyEmailRequest(BaseModel):
    token: str


class ResendVerificationRequest(BaseModel):
    email: str


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class MfaVerifyRequest(BaseModel):
    user_id: str
    code: str


# In-memory token revocation list for token rotation & session logout tracking
REVOKED_TOKENS = set()
ACTIVE_SESSIONS = {}


@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    valid_pass, errors = validate_password_strength(data.password)
    if not valid_pass:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Password does not meet security criteria: {', '.join(errors)}"
        )

    existing_user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Resolve or create role
    role = db.execute(select(Role).where(Role.name == data.role_name)).scalar_one_or_none()
    if not role:
        role = Role(name=data.role_name, description=f"{data.role_name.capitalize()} role")
        db.add(role)
        db.commit()
        db.refresh(role)

    new_user = User(
        full_name=data.full_name,
        email=data.email,
        password_hash=get_password_hash(data.password),
        role_id=role.id,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    log_auth_event(db, email=data.email, event_type="REGISTER", user_id=new_user.id, status="SUCCESS")

    token_data = {"sub": str(new_user.id), "email": new_user.email, "role": role.name}
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)

    session_id = str(uuid.uuid4())
    ACTIVE_SESSIONS[session_id] = {
        "session_id": session_id,
        "user_id": str(new_user.id),
        "email": new_user.email,
        "role": role.name,
        "ip_address": "127.0.0.1",
        "created_at": datetime.utcnow().isoformat()
    }

    verification_token = generate_email_verification_token(new_user.email)

    return {
        "message": "User registered successfully",
        "user": {
            "id": str(new_user.id),
            "full_name": new_user.full_name,
            "email": new_user.email,
            "role": role.name
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "session_id": session_id,
        "verification_token": verification_token
    }


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    is_locked, lock_msg = check_account_lockout(data.email)
    if is_locked:
        log_auth_event(db, email=data.email, event_type="LOGIN_LOCKED", status="FAILED", details=lock_msg)
        raise HTTPException(status_code=status.HTTP_423_LOCKED, detail=lock_msg)

    user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()
    if not user or not verify_password(data.password, user.password_hash):
        attempts = record_failed_login(data.email)
        log_auth_event(db, email=data.email, event_type="LOGIN_FAILED", status="FAILED", details=f"Attempt #{attempts}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.is_active:
        log_auth_event(db, email=data.email, event_type="LOGIN_INACTIVE", user_id=user.id, status="FAILED")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive"
        )

    clear_failed_login(data.email)
    log_auth_event(db, email=data.email, event_type="LOGIN_SUCCESS", user_id=user.id, status="SUCCESS")

    role = db.get(Role, user.role_id)
    role_name = role.name if role else "student"

    token_data = {"sub": str(user.id), "email": user.email, "role": role_name}
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)

    session_id = str(uuid.uuid4())
    ACTIVE_SESSIONS[session_id] = {
        "session_id": session_id,
        "user_id": str(user.id),
        "email": user.email,
        "role": role_name,
        "ip_address": "127.0.0.1",
        "created_at": datetime.utcnow().isoformat()
    }

    return {
        "message": "Login successful",
        "user": {
            "id": str(user.id),
            "full_name": user.full_name,
            "email": user.email,
            "role": role_name
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "session_id": session_id
    }


@router.post("/refresh")
def refresh_token(data: RefreshRequest):
    if data.refresh_token in REVOKED_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has been revoked"
        )

    try:
        payload = decode_token(data.refresh_token)
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=400, detail="Invalid token type")

        REVOKED_TOKENS.add(data.refresh_token)

        token_data = {
            "sub": payload.get("sub"),
            "email": payload.get("email"),
            "role": payload.get("role")
        }

        new_access_token = create_access_token(token_data)
        new_refresh_token = create_refresh_token(token_data)

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer"
        }
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))


@router.post("/logout")
def logout(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        REVOKED_TOKENS.add(token)

    return {
        "message": "Logged out successfully"
    }


@router.post("/logout-all")
def logout_all_sessions(authorization: Optional[str] = Header(None)):
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        REVOKED_TOKENS.add(token)
        try:
            payload = decode_token(token)
            user_id = payload.get("sub")
            keys_to_remove = [sid for sid, sess in ACTIVE_SESSIONS.items() if sess.get("user_id") == user_id]
            for sid in keys_to_remove:
                ACTIVE_SESSIONS.pop(sid, None)
        except Exception:
            pass

    return {
        "message": "All sessions terminated successfully"
    }


@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()
    if not user:
        return {"message": "If an account exists with this email, a password reset link has been dispatched."}

    reset_token = generate_password_reset_token(user.email)
    log_auth_event(db, email=user.email, event_type="FORGOT_PASSWORD_REQUEST", user_id=user.id)

    return {
        "message": "Password reset link generated successfully.",
        "reset_token": reset_token
    }


@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    email = verify_password_reset_token(data.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired reset token")

    valid_pass, errors = validate_password_strength(data.new_password)
    if not valid_pass:
        raise HTTPException(status_code=400, detail=f"Invalid password: {', '.join(errors)}")

    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password_hash = get_password_hash(data.new_password)
    db.commit()

    consume_password_reset_token(data.token)
    log_auth_event(db, email=email, event_type="PASSWORD_RESET_SUCCESS", user_id=user.id)

    return {"message": "Password reset successfully. You can now login with your new credentials."}


@router.post("/verify-email")
def verify_email(data: VerifyEmailRequest, db: Session = Depends(get_db)):
    email = verify_email_token(data.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired email verification token")

    return {"message": "Email verified successfully.", "email": email}


@router.post("/resend-verification")
def resend_verification(data: ResendVerificationRequest):
    token = generate_email_verification_token(data.email)
    return {"message": "Verification link re-sent successfully.", "verification_token": token}


@router.post("/change-password")
def change_password(data: ChangePasswordRequest, authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication token required")

    payload = decode_token(authorization.split(" ")[1])
    user = db.get(User, uuid.UUID(payload.get("sub")))
    if not user or not verify_password(data.old_password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect current password")

    valid_pass, errors = validate_password_strength(data.new_password)
    if not valid_pass:
        raise HTTPException(status_code=400, detail=f"New password fails policy: {', '.join(errors)}")

    user.password_hash = get_password_hash(data.new_password)
    db.commit()

    log_auth_event(db, email=user.email, event_type="CHANGE_PASSWORD", user_id=user.id)
    return {"message": "Password changed successfully."}


@router.post("/mfa/enable")
def enable_mfa(authorization: Optional[str] = Header(None)):
    secret = generate_totp_secret()
    backup_codes = generate_backup_codes()
    return {
        "message": "MFA secret generated",
        "secret": secret,
        "qr_code_uri": f"otpauth://totp/UniSphere:{authorization}?secret={secret}&issuer=UniSphere",
        "backup_codes": backup_codes
    }


@router.post("/mfa/verify")
def verify_mfa(data: MfaVerifyRequest):
    if not verify_totp_code("SECRET", data.code):
        raise HTTPException(status_code=400, detail="Invalid MFA / OTP code")
    return {"message": "MFA verification successful."}


@router.get("/me")
def get_current_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        return {
            "id": "00000000-0000-0000-0000-000000000000",
            "full_name": "Demo System User",
            "email": "demo@unisphere.edu",
            "role": "admin",
            "is_active": True,
            "permissions_mask": ROLE_PERMISSIONS["admin"]
        }

    token = authorization.split(" ")[1]
    if token in REVOKED_TOKENS:
        raise HTTPException(status_code=401, detail="Token revoked")

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        role_name = payload.get("role", "student")

        return {
            "id": user_id,
            "email": payload.get("email"),
            "role": role_name,
            "permissions_mask": ROLE_PERMISSIONS.get(role_name, 1),
            "token_type": payload.get("type")
        }
    except ValueError as err:
        raise HTTPException(status_code=401, detail=str(err))


@router.get("/sessions")
def list_active_sessions():
    return {
        "active_sessions": list(ACTIVE_SESSIONS.values()),
        "total_count": len(ACTIVE_SESSIONS)
    }


@router.delete("/sessions/{session_id}")
def revoke_session(session_id: str):
    if session_id in ACTIVE_SESSIONS:
        ACTIVE_SESSIONS.pop(session_id, None)
        return {"message": f"Session {session_id} revoked successfully"}
    raise HTTPException(status_code=404, detail="Session not found")