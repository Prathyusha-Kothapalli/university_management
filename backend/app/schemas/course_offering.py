from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CourseOfferingCreate(BaseModel):
    course_id: UUID
    academic_year_id: UUID
    semester_id: UUID
    is_active: bool = True


class CourseOfferingUpdate(BaseModel):
    course_id: UUID | None = None
    academic_year_id: UUID | None = None
    semester_id: UUID | None = None
    is_active: bool | None = None


class CourseOfferingResponse(BaseModel):
    id: UUID
    course_id: UUID
    academic_year_id: UUID
    semester_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)