from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.tenant import Tenant
from app.models.user import User, UserRole
from app.schemas.tenant import TenantOut, TenantCreate, TenantUpdate
from app.core.deps import get_current_active_user, require_roles, enforce_tenant_isolation

router = APIRouter(prefix="/tenants", tags=["Tenants"])

@router.get("", response_model=List[TenantOut])
def list_tenants(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    List universities/tenants.
    - Super Admin: Returns all tenants.
    - University Admin / Faculty / Student: Returns their own tenant institution only.
    """
    if current_user.role == UserRole.SUPER_ADMIN:
        return db.query(Tenant).order_by(Tenant.created_at.desc()).all()
    
    if current_user.tenant_id:
        tenant = db.query(Tenant).filter(Tenant.id == current_user.tenant_id).first()
        return [tenant] if tenant else []
    
    return []

@router.get("/{tenant_id}", response_model=TenantOut)
def get_tenant_by_id(
    tenant_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    Get detailed information for a specific tenant.
    """
    enforce_tenant_isolation(current_user, tenant_id)
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant institution not found",
        )
    return tenant

@router.post("", response_model=TenantOut, status_code=status.HTTP_201_CREATED)
def create_tenant(
    tenant_in: TenantCreate,
    current_user: User = Depends(require_roles(UserRole.SUPER_ADMIN)),
    db: Session = Depends(get_db)
) -> Any:
    """
    Create a new tenant institution (Restricted to Super Admin).
    """
    existing = db.query(Tenant).filter(
        (Tenant.code == tenant_in.code.upper()) | 
        (Tenant.name == tenant_in.name)
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tenant with code '{tenant_in.code}' or name '{tenant_in.name}' already exists",
        )
    
    tenant = Tenant(
        name=tenant_in.name,
        code=tenant_in.code.upper(),
        domain=tenant_in.domain.lower() if tenant_in.domain else None,
        description=tenant_in.description,
        is_active=tenant_in.is_active
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

@router.put("/{tenant_id}", response_model=TenantOut)
def update_tenant(
    tenant_id: str,
    tenant_in: TenantUpdate,
    current_user: User = Depends(require_roles(UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN)),
    db: Session = Depends(get_db)
) -> Any:
    """
    Update tenant institution details.
    """
    enforce_tenant_isolation(current_user, tenant_id)
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant institution not found",
        )
    
    if tenant_in.name is not None:
        tenant.name = tenant_in.name
    if tenant_in.code is not None:
        tenant.code = tenant_in.code.upper()
    if tenant_in.domain is not None:
        tenant.domain = tenant_in.domain.lower() if tenant_in.domain else None
    if tenant_in.description is not None:
        tenant.description = tenant_in.description
    
    # Only Super Admin can deactivate an entire university
    if tenant_in.is_active is not None and current_user.role == UserRole.SUPER_ADMIN:
        tenant.is_active = tenant_in.is_active

    db.commit()
    db.refresh(tenant)
    return tenant

