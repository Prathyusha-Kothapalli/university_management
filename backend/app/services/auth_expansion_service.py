import hashlib
import secrets
import uuid
from datetime import datetime, timedelta
from typing import List, Tuple, Optional
from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.user_session import UserSession
from app.models.mfa_recovery import MfaRecoveryCode
from app.models.auth_policy import AuthPolicy
from app.models.auth_audit import AuthAudit
from app.schemas.auth_expansion import SuspiciousLoginCheckResponse, AuthPolicySchema


def evaluate_login_risk(
    db: Session,
    user_id: uuid.UUID,
    ip_address: str,
    user_agent: str
) -> SuspiciousLoginCheckResponse:
    risk_score = 0.0
    reasons = []

    # Check previous sessions for user
    prev_sessions = db.execute(
        select(UserSession)
        .where(UserSession.user_id == user_id)
        .order_by(UserSession.created_at.desc())
        .limit(10)
    ).scalars().all()

    if prev_sessions:
        known_ips = {s.ip_address for s in prev_sessions}
        known_agents = {s.user_agent for s in prev_sessions}

        if ip_address not in known_ips:
            risk_score += 0.35
            reasons.append(f"Login from new IP address: {ip_address}")

        if user_agent not in known_agents:
            risk_score += 0.25
            reasons.append("Login from new User-Agent or browser environment")
    else:
        risk_score += 0.1
        reasons.append("First-time login detected on new device")

    # Check failed login count in recent 15 minutes
    fifteen_mins_ago = datetime.utcnow() - timedelta(minutes=15)
    recent_failed_attempts = db.execute(
        select(func.count(AuthAudit.id))
        .where(
            and_(
                AuthAudit.user_id == user_id,
                AuthAudit.status == "FAILED",
                AuthAudit.created_at >= fifteen_mins_ago
            )
        )
    ).scalar() or 0

    if recent_failed_attempts > 3:
        risk_score += 0.4
        reasons.append(f"Multiple recent failed login attempts ({recent_failed_attempts} failures in 15 mins)")

    action = "ALLOW"
    if risk_score >= 0.7:
        action = "MFA_CHALLENGE"
    elif risk_score >= 0.9:
        action = "BLOCK"

    return SuspiciousLoginCheckResponse(
        is_suspicious=risk_score >= 0.35,
        risk_score=min(round(risk_score, 2), 1.0),
        reasons=reasons,
        action_required=action
    )


def create_user_session(
    db: Session,
    user_id: uuid.UUID,
    session_token: str,
    ip_address: str,
    user_agent: str,
    device_type: str = "desktop",
    operating_system: str = "Windows",
    browser: str = "Chrome",
    duration_hours: int = 24
) -> UserSession:
    risk_info = evaluate_login_risk(db, user_id, ip_address, user_agent)
    
    expires_at = datetime.utcnow() + timedelta(hours=duration_hours)
    session = UserSession(
        user_id=user_id,
        session_token=session_token,
        ip_address=ip_address,
        user_agent=user_agent,
        device_type=device_type,
        operating_system=operating_system,
        browser=browser,
        anomaly_risk_score=risk_info.risk_score,
        expires_at=expires_at,
        is_active=True
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def generate_mfa_recovery_codes(db: Session, user_id: uuid.UUID) -> List[str]:
    # Invalidate existing codes
    existing_codes = db.execute(
        select(MfaRecoveryCode).where(MfaRecoveryCode.user_id == user_id)
    ).scalars().all()
    for code_obj in existing_codes:
        db.delete(code_obj)
    db.commit()

    raw_codes = []
    for _ in range(8):
        raw_code = secrets.token_hex(4).upper() # e.g. "A1B2C3D4"
        formatted_code = f"{raw_code[:4]}-{raw_code[4:]}"
        raw_codes.append(formatted_code)

        code_hash = hashlib.sha256(formatted_code.encode("utf-8")).hexdigest()
        mfa_code_entry = MfaRecoveryCode(
            user_id=user_id,
            code_hash=code_hash,
            is_used=False
        )
        db.add(mfa_code_entry)

    db.commit()
    return raw_codes


def verify_and_consume_recovery_code(db: Session, email: str, recovery_code: str) -> bool:
    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not user:
        return False

    code_hash = hashlib.sha256(recovery_code.strip().encode("utf-8")).hexdigest()
    mfa_entry = db.execute(
        select(MfaRecoveryCode).where(
            and_(
                MfaRecoveryCode.user_id == user.id,
                MfaRecoveryCode.code_hash == code_hash,
                MfaRecoveryCode.is_used == False
            )
        )
    ).scalar_one_or_none()

    if not mfa_entry:
        return False

    mfa_entry.is_used = True
    mfa_entry.used_at = datetime.utcnow()
    db.commit()
    return True


def evaluate_auth_policy(db: Session, university_id: Optional[uuid.UUID], password: str) -> Tuple[bool, List[str]]:
    policy = None
    if university_id:
        policy = db.execute(
            select(AuthPolicy).where(AuthPolicy.university_id == university_id)
        ).scalar_one_or_none()

    if not policy:
        # Default global policy
        policy = AuthPolicy(
            min_length=8,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_symbols=True
        )

    errors = []
    if len(password) < policy.min_length:
        errors.append(f"Password must be at least {policy.min_length} characters long")
    if policy.require_uppercase and not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter")
    if policy.require_lowercase and not any(c.islower() for c in password):
        errors.append("Password must contain at least one lowercase letter")
    if policy.require_digits and not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one numeric digit")
    if policy.require_symbols and not any(not c.isalnum() for c in password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")

    return len(errors) == 0, errors
