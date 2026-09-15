from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CourseCreate(BaseModel):
    program_id: UUID
    name: str
    code: str
    description: str | None = None
    credits: int
    is_active: bool = True


class CourseUpdate(BaseModel):
    program_id: UUID | None = None
    name: str | None = None
    code: str | None = None
    description: str | None = None
    credits: int | None = None
    is_active: bool | None = None


class CourseResponse(BaseModel):
    id: UUID
    program_id: UUID
    name: str
    code: str
    description: str | None
    credits: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)