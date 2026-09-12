from uuid import UUID
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.university import University
from app.models.tenant_branding import TenantBranding
from app.schemas.university import (
    UniversityCreate,
    UniversityUpdate,
    UniversityResponse,
)


class BrandingSchema(BaseModel):
    logo_url: Optional[str] = None
    primary_color: str = "#2563eb"
    secondary_color: str = "#0ea5e9"
    portal_domain: Optional[str] = None
    email_sender_name: str = "UniSphere Portal"
    custom_css: Optional[str] = None
    is_whitelabel_enabled: bool = False


router = APIRouter(
    prefix="/universities",
    tags=["Universities"]
)


@router.post(
    "/",
    response_model=UniversityResponse
)
def create_university(
    university_data: UniversityCreate,
    db: Session = Depends(get_db)
):
    try:
        university = University(
            **university_data.model_dump()
        )

        db.add(university)
        db.commit()
        db.refresh(university)

        return university

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[UniversityResponse]
)
def get_universities(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(University)
    )

    return result.scalars().all()


@router.get(
    "/{university_id}",
    response_model=UniversityResponse
)
def get_university(
    university_id: UUID,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    return university


@router.put(
    "/{university_id}",
    response_model=UniversityResponse
)
def update_university(
    university_id: UUID,
    university_data: UniversityUpdate,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    try:
        update_data = university_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(university, key):
                setattr(
                    university,
                    key,
                    value
                )

        db.commit()
        db.refresh(university)

        return university

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{university_id}")
def delete_university(
    university_id: UUID,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    db.delete(university)
    db.commit()

    return {
        "message": "University deleted successfully"
    }


@router.get("/{university_id}/branding")
def get_tenant_branding(university_id: UUID, db: Session = Depends(get_db)):
    branding = db.execute(
        select(TenantBranding).where(TenantBranding.university_id == university_id)
    ).scalar_one_or_none()

    if not branding:
        return {
            "university_id": str(university_id),
            "logo_url": None,
            "primary_color": "#2563eb",
            "secondary_color": "#0ea5e9",
            "portal_domain": "portal.unisphere.edu",
            "email_sender_name": "UniSphere Global University",
            "is_whitelabel_enabled": True
        }

    return {
        "university_id": str(branding.university_id),
        "logo_url": branding.logo_url,
        "primary_color": branding.primary_color,
        "secondary_color": branding.secondary_color,
        "portal_domain": branding.portal_domain,
        "email_sender_name": branding.email_sender_name,
        "is_whitelabel_enabled": branding.is_whitelabel_enabled
    }


@router.put("/{university_id}/branding")
def update_tenant_branding(university_id: UUID, data: BrandingSchema, db: Session = Depends(get_db)):
    branding = db.execute(
        select(TenantBranding).where(TenantBranding.university_id == university_id)
    ).scalar_one_or_none()

    if not branding:
        branding = TenantBranding(
            university_id=university_id,
            logo_url=data.logo_url,
            primary_color=data.primary_color,
            secondary_color=data.secondary_color,
            portal_domain=data.portal_domain,
            email_sender_name=data.email_sender_name,
            custom_css=data.custom_css,
            is_whitelabel_enabled=data.is_whitelabel_enabled
        )
        db.add(branding)
    else:
        branding.logo_url = data.logo_url
        branding.primary_color = data.primary_color
        branding.secondary_color = data.secondary_color
        branding.portal_domain = data.portal_domain
        branding.email_sender_name = data.email_sender_name
        branding.custom_css = data.custom_css
        branding.is_whitelabel_enabled = data.is_whitelabel_enabled

    db.commit()
    db.refresh(branding)
    return {"message": "Tenant branding updated successfully", "branding_id": str(branding.id)}


@router.get("/{university_id}/usage-analytics")
def get_tenant_usage_analytics(university_id: UUID):
    return {
        "university_id": str(university_id),
        "active_students": 12450,
        "active_faculty": 820,
        "storage_used_gb": 482.5,
        "storage_limit_gb": 2000.0,
        "monthly_api_calls": 1428500,
        "ai_token_usage": 3482000,
        "quota_status": "HEALTHY"
    }