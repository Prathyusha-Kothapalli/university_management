from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LearningMaterialCreate(BaseModel):
    course_offering_id: UUID
    faculty_id: UUID
    title: str
    description: str | None = None
    file_url: str | None = None
    material_type: str = "DOCUMENT"


class LearningMaterialUpdate(BaseModel):
    course_offering_id: UUID | None = None
    faculty_id: UUID | None = None
    title: str | None = None
    description: str | None = None
    file_url: str | None = None
    material_type: str | None = None


class LearningMaterialResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    faculty_id: UUID
    title: str
    description: str | None
    file_url: str | None
    material_type: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
