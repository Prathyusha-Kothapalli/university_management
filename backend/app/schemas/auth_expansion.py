from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class DeviceSessionResponse(BaseModel):
    id: UUID
    user_id: UUID
    ip_address: str
    user_agent: str
    device_type: str
    operating_system: str
    browser: str
    country: Optional[str] = None
    city: Optional[str] = None
    anomaly_risk_score: float
    is_trusted_device: bool
    is_active: bool
    last_active_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class MfaRecoverySetupResponse(BaseModel):
    user_id: UUID
    recovery_codes: List[str]
    created_at: datetime


class MfaRecoveryVerifyRequest(BaseModel):
    email: EmailStr
    recovery_code: str


class AuthPolicySchema(BaseModel):
    university_id: Optional[UUID] = None
    min_length: int = Field(8, ge=6, le=64)
    require_uppercase: bool = True
    require_lowercase: bool = True
    require_digits: bool = True
    require_symbols: bool = True
    max_login_attempts: int = Field(5, ge=3, le=20)
    lockout_duration_minutes: int = Field(15, ge=5, le=1440)
    session_idle_timeout_minutes: int = Field(30, ge=5, le=1440)
    mfa_required_roles: str = "admin,hod"

    class Config:
        from_attributes = True


class AuthAuditFilterRequest(BaseModel):
    email: Optional[str] = None
    event_type: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    limit: int = Field(50, ge=1, le=500)
    offset: int = Field(0, ge=0)


class SuspiciousLoginCheckResponse(BaseModel):
    is_suspicious: bool
    risk_score: float
    reasons: List[str]
    action_required: str # e.g. "ALLOW", "MFA_CHALLENGE", "BLOCK"
