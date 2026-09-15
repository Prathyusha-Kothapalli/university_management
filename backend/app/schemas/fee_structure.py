from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class FeeStructureCreate(BaseModel):
    university_id: UUID
    program_id: UUID
    academic_year_id: UUID
    name: str
    amount: float
    due_date: datetime


class FeeStructureUpdate(BaseModel):
    university_id: UUID | None = None
    program_id: UUID | None = None
    academic_year_id: UUID | None = None
    name: str | None = None
    amount: float | None = None
    due_date: datetime | None = None


class FeeStructureResponse(BaseModel):
    id: UUID
    university_id: UUID
    program_id: UUID
    academic_year_id: UUID
    name: str
    amount: float
    due_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
