import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.session import get_db
from app.models.university import University
from app.models.tenant_branding import TenantBranding
from app.models.tenant_invitation import TenantInvitation
from app.models.tenant_feature_flag import TenantFeatureFlag
from app.schemas.tenancy_expansion import (
    TenantBrandingCreateUpdate,
    TenantBrandingResponse,
    TenantInvitationCreate,
    TenantInvitationResponse,
    TenantStorageUsageResponse,
    TenantFeatureFlagSchema,
)
from app.services.tenancy_service import (
    onboard_new_tenant,
    update_tenant_branding,
    generate_tenant_css_theme,
    create_tenant_invitation,
    get_tenant_storage_status,
    is_feature_enabled_for_tenant,
)
from app.core.security import decode_token

router = APIRouter(
    prefix="/tenancy",
    tags=["Multi-Tenancy Management"]
)


@router.post("/onboard", response_model=TenantBrandingResponse)
def onboard_tenant(
    name: str,
    code: str,
    admin_email: str,
    domain: Optional[str] = None,
    db: Session = Depends(get_db)
):
    try:
        uni, branding = onboard_new_tenant(db, name, code, admin_email, domain)
        return branding
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))


@router.get("/{university_id}/branding", response_model=TenantBrandingResponse)
def get_branding(university_id: uuid.UUID, db: Session = Depends(get_db)):
    branding = db.execute(
        select(TenantBranding).where(TenantBranding.university_id == university_id)
    ).scalar_one_or_none()

    if not branding:
        raise HTTPException(status_code=404, detail="Branding not configured for this tenant")
    return branding


@router.put("/{university_id}/branding", response_model=TenantBrandingResponse)
def update_branding(
    university_id: uuid.UUID,
    data: TenantBrandingCreateUpdate,
    db: Session = Depends(get_db)
):
    return update_tenant_branding(db, university_id, data)


@router.get("/{university_id}/theme.css")
def get_tenant_css(university_id: uuid.UUID, db: Session = Depends(get_db)):
    branding = db.execute(
        select(TenantBranding).where(TenantBranding.university_id == university_id)
    ).scalar_one_or_none()

    if not branding:
        branding = TenantBranding(university_id=university_id)

    css_content = generate_tenant_css_theme(branding)
    return {"css": css_content}


@router.post("/{university_id}/invitations", response_model=TenantInvitationResponse)
def invite_tenant_user(
    university_id: uuid.UUID,
    data: TenantInvitationCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    user_id = uuid.uuid4()
    if authorization and authorization.startswith("Bearer "):
        payload = decode_token(authorization.split(" ")[1])
        user_id = uuid.UUID(payload.get("sub"))

    invitation = create_tenant_invitation(db, university_id, user_id, data)
    return invitation


@router.get("/{university_id}/storage", response_model=TenantStorageUsageResponse)
def get_storage_usage(university_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_tenant_storage_status(db, university_id)


@router.get("/{university_id}/feature-flags", response_model=List[TenantFeatureFlagSchema])
def list_feature_flags(university_id: uuid.UUID, db: Session = Depends(get_db)):
    flags = db.execute(
        select(TenantFeatureFlag).where(TenantFeatureFlag.university_id == university_id)
    ).scalars().all()

    return [
        TenantFeatureFlagSchema(
            feature_key=f.feature_key,
            is_enabled=f.is_enabled,
            description=f.description
        )
        for f in flags
    ]


@router.put("/{university_id}/feature-flags/{feature_key}")
def toggle_feature_flag(
    university_id: uuid.UUID,
    feature_key: str,
    enabled: bool,
    db: Session = Depends(get_db)
):
    flag = db.execute(
        select(TenantFeatureFlag).where(
            TenantFeatureFlag.university_id == university_id,
            TenantFeatureFlag.feature_key == feature_key
        )
    ).scalar_one_or_none()

    if not flag:
        flag = TenantFeatureFlag(
            university_id=university_id,
            feature_key=feature_key,
            is_enabled=enabled
        )
        db.add(flag)
    else:
        flag.is_enabled = enabled

    db.commit()
    return {"message": f"Feature '{feature_key}' updated to {enabled}"}
