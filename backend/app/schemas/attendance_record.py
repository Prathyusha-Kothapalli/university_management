from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AttendanceRecordCreate(BaseModel):
    attendance_session_id: UUID
    student_id: UUID
    status: str = "PRESENT"
    marked_at: datetime | None = None
    remarks: str | None = None


class AttendanceRecordUpdate(BaseModel):
    attendance_session_id: UUID | None = None
    student_id: UUID | None = None
    status: str | None = None
    marked_at: datetime | None = None
    remarks: str | None = None


class AttendanceRecordResponse(BaseModel):
    id: UUID
    attendance_session_id: UUID
    student_id: UUID
    status: str
    marked_at: datetime | None
    remarks: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)