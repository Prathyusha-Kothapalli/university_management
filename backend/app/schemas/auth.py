from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole
from app.schemas.user import UserOut
from app.schemas.tenant import TenantOut

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    role: Optional[str] = None
    tenant_id: Optional[str] = None
    exp: Optional[int] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_code: Optional[str] = None

class RegisterTenantRequest(BaseModel):
    # University/Tenant Details
    tenant_name: str = Field(..., min_length=2, max_length=255)
    tenant_code: str = Field(..., min_length=2, max_length=50)
    tenant_domain: Optional[str] = Field(None, max_length=255)
    tenant_description: Optional[str] = None

    # Initial University Admin Account
    admin_email: EmailStr
    admin_password: str = Field(..., min_length=6, max_length=128)
    admin_name: str = Field(..., min_length=2, max_length=255)
    admin_department: Optional[str] = "University Administration"

class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)
    full_name: str = Field(..., min_length=2, max_length=255)
    role: UserRole = UserRole.STUDENT
    tenant_id: Optional[str] = None
    department: Optional[str] = None
    phone_number: Optional[str] = None

