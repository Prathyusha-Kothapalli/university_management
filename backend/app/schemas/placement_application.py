from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PlacementApplicationCreate(BaseModel):
    placement_drive_id: UUID
    student_id: UUID
    application_date: datetime | None = None
    status: str = "APPLIED"
    resume_url: str | None = None


class PlacementApplicationUpdate(BaseModel):
    placement_drive_id: UUID | None = None
    student_id: UUID | None = None
    application_date: datetime | None = None
    status: str | None = None
    resume_url: str | None = None


class PlacementApplicationResponse(BaseModel):
    id: UUID
    placement_drive_id: UUID
    student_id: UUID
    application_date: datetime
    status: str
    resume_url: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
