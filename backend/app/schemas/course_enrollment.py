from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CourseEnrollmentCreate(BaseModel):
    course_offering_id: UUID
    student_id: UUID
    enrollment_date: datetime | None = None
    status: str = "ENROLLED"


class CourseEnrollmentUpdate(BaseModel):
    course_offering_id: UUID | None = None
    student_id: UUID | None = None
    enrollment_date: datetime | None = None
    status: str | None = None


class CourseEnrollmentResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    student_id: UUID
    enrollment_date: datetime
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)