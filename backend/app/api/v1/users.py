from typing import List, Optional, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User, UserRole
from app.schemas.user import UserOut, UserUpdate
from app.core.deps import get_current_active_user, require_roles, enforce_tenant_isolation
from app.core.security import get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=List[UserOut])
def list_users(
    tenant_id: Optional[str] = Query(None, description="Filter by tenant ID (Super Admin only)"),
    role: Optional[UserRole] = Query(None, description="Filter by role"),
    department: Optional[str] = Query(None, description="Filter by department"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    List users with tenant isolation:
    - Super Admin can list users from any tenant or all tenants.
    - University Admin, Faculty, and Staff can list users only from their own tenant.
    - Students can list peers/faculty in their tenant.
    """
    query = db.query(User)

    if current_user.role == UserRole.SUPER_ADMIN:
        if tenant_id:
            query = query.filter(User.tenant_id == tenant_id)
    else:
        # Strict tenant boundary enforcement
        query = query.filter(User.tenant_id == current_user.tenant_id)
    
    if role:
        query = query.filter(User.role == role)
    if department:
        query = query.filter(User.department.ilike(f"%{department}%"))

    return query.order_by(User.created_at.desc()).all()

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(
    user_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    Get user by ID with tenant isolation checks.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    if current_user.role != UserRole.SUPER_ADMIN:
        enforce_tenant_isolation(current_user, user.tenant_id)
        
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: str,
    user_in: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    Update a user profile. Admins can update roles/status; users can update their own profile.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Permission check: Self, Super Admin, or University Admin of same tenant
    is_self = current_user.id == user.id
    is_super = current_user.role == UserRole.SUPER_ADMIN
    is_tenant_admin = current_user.role == UserRole.UNIVERSITY_ADMIN and current_user.tenant_id == user.tenant_id

    if not (is_self or is_super or is_tenant_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this user",
        )
    
    if user_in.full_name is not None:
        user.full_name = user_in.full_name
    if user_in.department is not None:
        user.department = user_in.department
    if user_in.phone_number is not None:
        user.phone_number = user_in.phone_number
    if user_in.password:
        user.hashed_password = get_password_hash(user_in.password)
    
    # Privileged field updates
    if (is_super or is_tenant_admin) and user_in.role is not None:
        if is_tenant_admin and user_in.role in [UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="University Admin cannot elevate to Super Admin or duplicate University Admin",
            )
        user.role = user_in.role
    
    if (is_super or is_tenant_admin) and user_in.is_active is not None:
        user.is_active = user_in.is_active

    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: str,
    current_user: User = Depends(require_roles(UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN)),
    db: Session = Depends(get_db)
) -> None:
    """
    Delete or deactivate a user account.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    if current_user.role != UserRole.SUPER_ADMIN:
        enforce_tenant_isolation(current_user, user.tenant_id)
        if user.role in [UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot delete higher or equal tier administrator",
            )
    
    db.delete(user)
    db.commit()
    return None

