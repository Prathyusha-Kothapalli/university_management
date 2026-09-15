from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.tenant import Tenant
from app.models.user import User, UserRole
from app.schemas.auth import LoginRequest, RegisterTenantRequest, RegisterUserRequest, Token
from app.schemas.user import UserOut
from app.schemas.tenant import TenantOut
from app.core.security import get_password_hash, verify_password, create_access_token

class AuthService:
    @staticmethod
    def authenticate_user(db: Session, login_data: LoginRequest) -> Token:
        query = db.query(User).filter(User.email == login_data.email)
        user = query.first()

        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is deactivated",
            )
        
        # If tenant_code is provided and user is not SUPER_ADMIN, verify tenant match
        if login_data.tenant_code and user.role != UserRole.SUPER_ADMIN:
            tenant = db.query(Tenant).filter(Tenant.code.ilike(login_data.tenant_code)).first()
            if not tenant or tenant.id != user.tenant_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"User is not registered under tenant '{login_data.tenant_code}'",
                )
            if not tenant.is_active:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Institution/Tenant is currently deactivated",
                )
        
        # Generate token
        access_token = create_access_token(
            subject=user.id,
            role=user.role.value,
            tenant_id=user.tenant_id
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
            user=UserOut.model_validate(user)
        )

    @staticmethod
    def register_tenant(db: Session, reg_data: RegisterTenantRequest) -> Token:
        # Check tenant code / domain uniqueness
        existing_code = db.query(Tenant).filter(Tenant.code.ilike(reg_data.tenant_code)).first()
        if existing_code:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Tenant with code '{reg_data.tenant_code}' already exists",
            )
        
        if reg_data.tenant_domain:
            existing_domain = db.query(Tenant).filter(Tenant.domain.ilike(reg_data.tenant_domain)).first()
            if existing_domain:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Tenant with domain '{reg_data.tenant_domain}' already exists",
                )
        
        # Check admin email uniqueness
        existing_user = db.query(User).filter(User.email == reg_data.admin_email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email '{reg_data.admin_email}' already exists",
            )
        
        # Create tenant
        tenant = Tenant(
            name=reg_data.tenant_name,
            code=reg_data.tenant_code.upper(),
            domain=reg_data.tenant_domain.lower() if reg_data.tenant_domain else None,
            description=reg_data.tenant_description,
            is_active=True
        )
        db.add(tenant)
        db.flush()

        # Create university admin user
        admin_user = User(
            email=reg_data.admin_email,
            hashed_password=get_password_hash(reg_data.admin_password),
            full_name=reg_data.admin_name,
            role=UserRole.UNIVERSITY_ADMIN,
            tenant_id=tenant.id,
            department=reg_data.admin_department or "Administration",
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)

        # Generate access token
        access_token = create_access_token(
            subject=admin_user.id,
            role=admin_user.role.value,
            tenant_id=tenant.id
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
            user=UserOut.model_validate(admin_user)
        )

    @staticmethod
    def register_user_in_tenant(
        db: Session,
        reg_data: RegisterUserRequest,
        creator: Optional[User] = None
    ) -> User:
        # Check email uniqueness
        existing_user = db.query(User).filter(User.email == reg_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email '{reg_data.email}' already exists",
            )
        
        target_tenant_id = reg_data.tenant_id
        if creator:
            # If creator is UNIVERSITY_ADMIN, they can only create users in their tenant
            if creator.role == UserRole.UNIVERSITY_ADMIN:
                target_tenant_id = creator.tenant_id
                if reg_data.role in [UserRole.SUPER_ADMIN, UserRole.UNIVERSITY_ADMIN]:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="University Admin cannot create Super Admin or University Admin roles directly",
                    )
            elif creator.role != UserRole.SUPER_ADMIN:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Only administrators can register new users",
                )

        if not target_tenant_id and reg_data.role != UserRole.SUPER_ADMIN:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="tenant_id is required for non-SuperAdmin users",
            )

        if target_tenant_id:
            tenant = db.query(Tenant).filter(Tenant.id == target_tenant_id).first()
            if not tenant:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Tenant '{target_tenant_id}' not found",
                )

        user = User(
            email=reg_data.email,
            hashed_password=get_password_hash(reg_data.password),
            full_name=reg_data.full_name,
            role=reg_data.role,
            tenant_id=target_tenant_id,
            department=reg_data.department,
            phone_number=reg_data.phone_number,
            is_active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

