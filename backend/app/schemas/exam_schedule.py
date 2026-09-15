from datetime import datetime, time
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExamScheduleCreate(BaseModel):
    exam_id: UUID
    classroom_id: UUID | None = None
    invigilator_faculty_id: UUID | None = None
    exam_date: datetime
    start_time: time | None = None
    end_time: time | None = None


class ExamScheduleUpdate(BaseModel):
    exam_id: UUID | None = None
    classroom_id: UUID | None = None
    invigilator_faculty_id: UUID | None = None
    exam_date: datetime | None = None
    start_time: time | None = None
    end_time: time | None = None


class ExamScheduleResponse(BaseModel):
    id: UUID
    exam_id: UUID
    classroom_id: UUID | None
    invigilator_faculty_id: UUID | None
    exam_date: datetime
    start_time: time | None
    end_time: time | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
