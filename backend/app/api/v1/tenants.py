import uuid
from typing import Dict, Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.tenancy import tenant_manager

router = APIRouter(
    prefix="/tenants",
    tags=["Multi-Tenancy"]
)


class TenantCreateRequest(BaseModel):
    name: str
    slug: str
    admin_email: str
    domain_cname: Optional[str] = None


class FeatureFlagUpdateRequest(BaseModel):
    feature_name: str
    enabled: bool


# In-memory tenant registry for fast lookup & execution
TENANTS_REGISTRY = {
    "default": {
        "id": "tenant-001",
        "name": "UniSphere Global University",
        "slug": "global",
        "schema_name": "public",
        "status": "ACTIVE"
    }
}


@router.post("/")
def register_tenant(req: TenantCreateRequest, db: Session = Depends(get_db)):
    if req.slug in TENANTS_REGISTRY:
        raise HTTPException(status_code=400, detail="Tenant with this slug already exists")

    schema_name = tenant_manager.sanitize_schema_name(req.slug)
    tenant_id = str(uuid.uuid4())

    entry = {
        "id": tenant_id,
        "name": req.name,
        "slug": req.slug,
        "schema_name": schema_name,
        "admin_email": req.admin_email,
        "domain_cname": req.domain_cname or f"{req.slug}.unisphere.edu",
        "status": "PROVISIONED",
        "created_at": "2026-09-11T12:00:00Z"
    }

    TENANTS_REGISTRY[req.slug] = entry
    tenant_manager.set_tenant_schema(db, req.slug)

    return {
        "message": "Tenant provisioned successfully",
        "tenant": entry,
        "feature_flags": tenant_manager.get_feature_flags(req.slug)
    }


@router.get("/")
def list_tenants():
    return {
        "total_tenants": len(TENANTS_REGISTRY),
        "tenants": list(TENANTS_REGISTRY.values())
    }


@router.get("/{tenant_slug}/feature-flags")
def get_tenant_feature_flags(tenant_slug: str):
    flags = tenant_manager.get_feature_flags(tenant_slug)
    return {
        "tenant_slug": tenant_slug,
        "feature_flags": flags
    }


@router.put("/{tenant_slug}/feature-flags")
def update_tenant_feature_flag(tenant_slug: str, req: FeatureFlagUpdateRequest):
    updated = tenant_manager.set_feature_flag(tenant_slug, req.feature_name, req.enabled)
    return {
        "message": f"Feature flag '{req.feature_name}' updated to {req.enabled}",
        "tenant_slug": tenant_slug,
        "feature_flags": updated
    }
