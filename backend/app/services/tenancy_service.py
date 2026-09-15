import uuid
import secrets
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any, Tuple
from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.models.university import University
from app.models.tenant_branding import TenantBranding
from app.models.tenant_invitation import TenantInvitation
from app.models.tenant_storage_log import TenantStorageLog
from app.models.tenant_feature_flag import TenantFeatureFlag
from app.models.campus import Campus
from app.models.classroom import Classroom
from app.schemas.tenancy_expansion import (
    TenantBrandingCreateUpdate,
    TenantInvitationCreate,
    TenantStorageUsageResponse
)


def onboard_new_tenant(
    db: Session,
    university_name: str,
    university_code: str,
    admin_email: str,
    domain: Optional[str] = None
) -> Tuple[University, TenantBranding]:
    existing = db.execute(
        select(University).where(University.code == university_code)
    ).scalar_one_or_none()
    if existing:
        raise ValueError(f"University with code '{university_code}' already exists")

    university = University(
        name=university_name,
        code=university_code,
        contact_email=admin_email,
        is_active=True
    )
    db.add(university)
    db.commit()
    db.refresh(university)

    # Initialize default branding
    branding = TenantBranding(
        university_id=university.id,
        primary_color="#1E40AF",
        secondary_color="#3B82F6",
        accent_color="#10B981",
        portal_title=f"{university_name} Portal",
        support_email=admin_email
    )
    db.add(branding)

    # Initialize default feature flags
    default_flags = [
        ("ai_copilot", True, "Enable AI study copilot & assistant"),
        ("qr_attendance", True, "Enable dynamic QR code attendance system"),
        ("obe_curriculum", True, "Enable Outcome-Based Education (OBE) tracking"),
        ("online_exams", True, "Enable online proctored exam engine"),
        ("placement_portal", True, "Enable placement & career hub"),
        ("hostel_management", True, "Enable hostel room allocation"),
        ("transport_tracking", True, "Enable transport & route optimization")
    ]
    for key, enabled, desc in default_flags:
        flag = TenantFeatureFlag(
            university_id=university.id,
            feature_key=key,
            is_enabled=enabled,
            description=desc
        )
        db.add(flag)

    # Initialize storage monitor record
    storage_log = TenantStorageLog(
        university_id=university.id,
        total_storage_bytes=0,
        storage_quota_bytes=107374182400, # 100GB default
        document_count=0,
        usage_percentage=0.0
    )
    db.add(storage_log)

    db.commit()
    db.refresh(branding)
    return university, branding


def update_tenant_branding(
    db: Session,
    university_id: uuid.UUID,
    branding_data: TenantBrandingCreateUpdate
) -> TenantBranding:
    branding = db.execute(
        select(TenantBranding).where(TenantBranding.university_id == university_id)
    ).scalar_one_or_none()

    if not branding:
        branding = TenantBranding(university_id=university_id)
        db.add(branding)

    for field, val in branding_data.dict(exclude_unset=True).items():
        setattr(branding, field, val)

    branding.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(branding)
    return branding


def generate_tenant_css_theme(branding: TenantBranding) -> str:
    return f"""
:root {{
  --color-primary: {branding.primary_color};
  --color-secondary: {branding.secondary_color};
  --color-accent: {branding.accent_color};
}}
.tenant-header {{
  background-color: var(--color-primary);
}}
.tenant-btn-primary {{
  background-color: var(--color-primary);
  color: #ffffff;
}}
.tenant-btn-accent {{
  background-color: var(--color-accent);
  color: #ffffff;
}}
"""


def create_tenant_invitation(
    db: Session,
    university_id: uuid.UUID,
    invited_by_id: uuid.UUID,
    invitation_data: TenantInvitationCreate
) -> TenantInvitation:
    token = secrets.token_urlsafe(32)
    expires = datetime.utcnow() + timedelta(days=7)

    invitation = TenantInvitation(
        university_id=university_id,
        email=invitation_data.email,
        role_name=invitation_data.role_name,
        invitation_token=token,
        invited_by_id=invited_by_id,
        expires_at=expires,
        is_accepted=False
    )
    db.add(invitation)
    db.commit()
    db.refresh(invitation)
    return invitation


def get_tenant_storage_status(db: Session, university_id: uuid.UUID) -> TenantStorageUsageResponse:
    log = db.execute(
        select(TenantStorageLog)
        .where(TenantStorageLog.university_id == university_id)
        .order_by(TenantStorageLog.recorded_at.desc())
    ).scalar_one_or_none()

    if not log:
        log = TenantStorageLog(
            university_id=university_id,
            total_storage_bytes=0,
            storage_quota_bytes=107374182400,
            document_count=0,
            usage_percentage=0.0
        )
        db.add(log)
        db.commit()
        db.refresh(log)

    return TenantStorageUsageResponse(
        university_id=university_id,
        total_storage_bytes=log.total_storage_bytes,
        storage_quota_bytes=log.storage_quota_bytes,
        document_count=log.document_count,
        usage_percentage=log.usage_percentage,
        recorded_at=log.recorded_at
    )


def is_feature_enabled_for_tenant(db: Session, university_id: uuid.UUID, feature_key: str) -> bool:
    flag = db.execute(
        select(TenantFeatureFlag).where(
            and_(
                TenantFeatureFlag.university_id == university_id,
                TenantFeatureFlag.feature_key == feature_key
            )
        )
    ).scalar_one_or_none()

    if not flag:
        return True # Default to enabled if flag not explicitly configured
    return flag.is_enabled
