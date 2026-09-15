import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, desc

from app.database.session import get_db
from app.models.user import User
from app.models.user_session import UserSession
from app.models.auth_audit import AuthAudit
from app.schemas.auth_expansion import (
    DeviceSessionResponse,
    MfaRecoverySetupResponse,
    MfaRecoveryVerifyRequest,
    AuthPolicySchema,
    SuspiciousLoginCheckResponse,
)
from app.services.auth_expansion_service import (
    evaluate_login_risk,
    generate_mfa_recovery_codes,
    verify_and_consume_recovery_code,
    evaluate_auth_policy,
)
from app.core.security import decode_token

router = APIRouter(
    prefix="/auth/expansion",
    tags=["Auth Expansion & Security"]
)


@router.get("/sessions/devices", response_model=List[DeviceSessionResponse])
def get_user_device_sessions(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication token required")

    payload = decode_token(authorization.split(" ")[1])
    user_id = uuid.UUID(payload.get("sub"))

    sessions = db.execute(
        select(UserSession)
        .where(and_(UserSession.user_id == user_id, UserSession.is_active == True))
        .order_by(desc(UserSession.last_active_at))
    ).scalars().all()

    return sessions


@router.post("/sessions/{session_id}/revoke")
def revoke_device_session(
    session_id: uuid.UUID,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication token required")

    payload = decode_token(authorization.split(" ")[1])
    user_id = uuid.UUID(payload.get("sub"))

    session_entry = db.get(UserSession, session_id)
    if not session_entry or session_entry.user_id != user_id:
        raise HTTPException(status_code=404, detail="Device session not found or unauthorized")

    session_entry.is_active = False
    db.commit()

    return {"message": "Device session successfully revoked"}


@router.post("/mfa/recovery-codes/generate", response_model=MfaRecoverySetupResponse)
def generate_recovery_codes(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication token required")

    payload = decode_token(authorization.split(" ")[1])
    user_id = uuid.UUID(payload.get("sub"))

    codes = generate_mfa_recovery_codes(db, user_id)
    return MfaRecoverySetupResponse(
        user_id=user_id,
        recovery_codes=codes,
        created_at=db.execute(select(UserSession.created_at)).scalar() or uuid.uuid4().int
    )


@router.post("/mfa/recovery-codes/verify")
def verify_recovery_code(
    data: MfaRecoveryVerifyRequest,
    db: Session = Depends(get_db)
):
    success = verify_and_consume_recovery_code(db, data.email, data.recovery_code)
    if not success:
        raise HTTPException(status_code=400, detail="Invalid or previously used recovery code")

    return {"message": "Recovery code verified. Access granted."}


@router.get("/risk-analysis", response_model=SuspiciousLoginCheckResponse)
def check_login_risk(
    user_id: uuid.UUID,
    ip_address: str = Query("127.0.0.1"),
    user_agent: str = Query("Mozilla/5.0"),
    db: Session = Depends(get_db)
):
    return evaluate_login_risk(db, user_id, ip_address, user_agent)


@router.get("/audit-logs")
def get_auth_audit_logs(
    email: Optional[str] = Query(None),
    event_type: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500),
    db: Session = Depends(get_db)
):
    stmt = select(AuthAudit)
    if email:
        stmt = stmt.where(AuthAudit.email == email)
    if event_type:
        stmt = stmt.where(AuthAudit.event_type == event_type)
    if status_filter:
        stmt = stmt.where(AuthAudit.status == status_filter)

    stmt = stmt.order_by(desc(AuthAudit.created_at)).limit(limit)
    logs = db.execute(stmt).scalars().all()

    return [
        {
            "id": str(log.id),
            "email": log.email,
            "event_type": log.event_type,
            "status": log.status,
            "ip_address": log.ip_address,
            "details": log.details,
            "created_at": log.created_at
        }
        for log in logs
    ]
