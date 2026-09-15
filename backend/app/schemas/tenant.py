from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class TenantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    code: str = Field(..., min_length=2, max_length=50)
    domain: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    is_active: bool = True

class TenantCreate(TenantBase):
    pass

class TenantUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    code: Optional[str] = Field(None, min_length=2, max_length=50)
    domain: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class TenantOut(TenantBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
