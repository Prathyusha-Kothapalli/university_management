from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AcademicYearCreate(BaseModel):
    university_id: UUID
    name: str
    start_date: date
    end_date: date
    is_current: bool = False


class AcademicYearUpdate(BaseModel):
    university_id: UUID | None = None
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    is_current: bool | None = None


class AcademicYearResponse(BaseModel):
    id: UUID
    university_id: UUID
    name: str
    start_date: date
    end_date: date
    is_current: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)