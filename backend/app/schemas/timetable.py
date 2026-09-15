from datetime import datetime, time
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TimetableCreate(BaseModel):
    course_offering_id: UUID
    classroom_id: UUID
    day_of_week: str
    start_time: time
    end_time: time
    is_active: bool = True


class TimetableUpdate(BaseModel):
    course_offering_id: UUID | None = None
    classroom_id: UUID | None = None
    day_of_week: str | None = None
    start_time: time | None = None
    end_time: time | None = None
    is_active: bool | None = None


class TimetableResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    classroom_id: UUID
    day_of_week: str
    start_time: time
    end_time: time
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)