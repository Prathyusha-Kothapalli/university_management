from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProgramCreate(BaseModel):
    department_id: UUID
    name: str
    code: str
    degree_type: str
    duration_years: int
    is_active: bool = True


class ProgramUpdate(BaseModel):
    department_id: UUID | None = None
    name: str | None = None
    code: str | None = None
    degree_type: str | None = None
    duration_years: int | None = None
    is_active: bool | None = None


class ProgramResponse(BaseModel):
    id: UUID
    department_id: UUID
    name: str
    code: str
    degree_type: str
    duration_years: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)