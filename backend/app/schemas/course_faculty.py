from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CourseFacultyCreate(BaseModel):
    course_offering_id: UUID
    faculty_id: UUID


class CourseFacultyUpdate(BaseModel):
    course_offering_id: UUID | None = None
    faculty_id: UUID | None = None


class CourseFacultyResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    faculty_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)