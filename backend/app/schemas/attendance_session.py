from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AttendanceSessionCreate(BaseModel):
    course_offering_id: UUID
    timetable_id: UUID | None = None
    session_date: datetime
    topic: str | None = None
    status: str = "OPEN"


class AttendanceSessionUpdate(BaseModel):
    course_offering_id: UUID | None = None
    timetable_id: UUID | None = None
    session_date: datetime | None = None
    topic: str | None = None
    status: str | None = None


class AttendanceSessionResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    timetable_id: UUID | None
    session_date: datetime
    topic: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)