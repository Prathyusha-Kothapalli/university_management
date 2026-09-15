from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.core.security import decode_access_token
from app.models.user import User, UserRole
from app.models.tenant import Tenant

security_scheme = HTTPBearer(auto_error=False)

def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    db: Session = Depends(get_db)
) -> User:
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    payload = decode_access_token(credentials.credentials)
    if not payload or not payload.get("sub"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Authenticated user no longer exists",
        )
    
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account",
        )
    
    # If user belongs to a tenant, check that the tenant is active
    if current_user.tenant_id and current_user.tenant and not current_user.tenant.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="University / Tenant institution is currently deactivated",
        )
        
    return current_user

def require_roles(*allowed_roles: UserRole):
    """
    Factory dependency for role-based access control.
    SUPER_ADMIN always has universal permission.
    """
    def role_checker(current_user: User = Depends(get_current_active_user)) -> User:
        if current_user.role == UserRole.SUPER_ADMIN:
            return current_user
        
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Allowed roles: {[r.value for r in allowed_roles]}, your role: {current_user.role.value}",
            )
        return current_user
    
    return role_checker

def get_tenant_context(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Optional[Tenant]:
    """
    Returns the Tenant of the current user, or None if SUPER_ADMIN without specific tenant.
    """
    if current_user.tenant_id:
        tenant = db.query(Tenant).filter(Tenant.id == current_user.tenant_id).first()
        return tenant
    return None

def enforce_tenant_isolation(current_user: User, target_tenant_id: Optional[str]) -> None:
    """
    Enforces that non-SUPER_ADMIN users cannot access or manipulate resources in another tenant.
    """
    if current_user.role == UserRole.SUPER_ADMIN:
        return
    
    if current_user.tenant_id != target_tenant_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cross-tenant access forbidden. You cannot access resources outside your institution.",
        )

