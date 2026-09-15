from typing import Any
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.auth import LoginRequest, RegisterTenantRequest, RegisterUserRequest, Token
from app.schemas.user import UserOut
from app.services.auth_service import AuthService
from app.core.deps import get_current_active_user, require_roles
from app.models.user import User, UserRole

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
) -> Any:
    """
    Authenticate user and generate JWT Bearer access token.
    Supports optional tenant_code matching.
    """
    return AuthService.authenticate_user(db=db, login_data=login_data)

@router.post("/register-tenant", response_model=Token, status_code=status.HTTP_201_CREATED)
def register_tenant(
    reg_data: RegisterTenantRequest,
    db: Session = Depends(get_db)
) -> Any:
    """
    Onboard a new university/tenant institution and create its root University Administrator.
    """
    return AuthService.register_tenant(db=db, reg_data=reg_data)

@router.post("/register-user", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(
    reg_data: RegisterUserRequest,
    current_user: User = Depends(require_roles(UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN)),
    db: Session = Depends(get_db)
) -> Any:
    """
    Register a new user (Student, Faculty, Staff) inside a tenant.
    Restricted to Super Admins and University Admins.
    """
    return AuthService.register_user_in_tenant(db=db, reg_data=reg_data, creator=current_user)

@router.get("/me", response_model=UserOut)
def read_current_user_profile(
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    Get profile information of the currently authenticated user with tenant context.
    """
    return current_user

