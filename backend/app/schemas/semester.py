from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SemesterCreate(BaseModel):
    academic_year_id: UUID
    name: str
    semester_number: int
    start_date: date
    end_date: date
    is_current: bool = False


class SemesterUpdate(BaseModel):
    academic_year_id: UUID | None = None
    name: str | None = None
    semester_number: int | None = None
    start_date: date | None = None
    end_date: date | None = None
    is_current: bool | None = None


class SemesterResponse(BaseModel):
    id: UUID
    academic_year_id: UUID
    name: str
    semester_number: int
    start_date: date
    end_date: date
    is_current: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)