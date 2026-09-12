from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DepartmentCreate(BaseModel):
    university_id: UUID
    campus_id: UUID
    name: str
    code: str
    description: str | None = None
    is_active: bool = True


class DepartmentUpdate(BaseModel):
    university_id: UUID | None = None
    campus_id: UUID | None = None
    name: str | None = None
    code: str | None = None
    description: str | None = None
    is_active: bool | None = None


class DepartmentResponse(BaseModel):
    id: UUID
    university_id: UUID
    campus_id: UUID
    name: str
    code: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)