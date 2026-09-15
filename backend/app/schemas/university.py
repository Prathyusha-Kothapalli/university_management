from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UniversityCreate(BaseModel):
    name: str
    code: str
    address: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None
    is_active: bool = True


class UniversityUpdate(BaseModel):
    name: str | None = None
    code: str | None = None
    address: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None
    is_active: bool | None = None


class UniversityResponse(BaseModel):
    id: UUID
    name: str
    code: str
    address: str | None
    contact_email: str | None
    contact_phone: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)