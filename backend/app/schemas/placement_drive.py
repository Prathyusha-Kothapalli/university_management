from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PlacementDriveCreate(BaseModel):
    university_id: UUID
    company_name: str
    job_title: str
    description: str | None = None
    eligibility_criteria: str | None = None
    package_details: str | None = None
    drive_date: datetime
    deadline: datetime
    status: str = "UPCOMING"


class PlacementDriveUpdate(BaseModel):
    university_id: UUID | None = None
    company_name: str | None = None
    job_title: str | None = None
    description: str | None = None
    eligibility_criteria: str | None = None
    package_details: str | None = None
    drive_date: datetime | None = None
    deadline: datetime | None = None
    status: str | None = None


class PlacementDriveResponse(BaseModel):
    id: UUID
    university_id: UUID
    company_name: str
    job_title: str
    description: str | None
    eligibility_criteria: str | None
    package_details: str | None
    drive_date: datetime
    deadline: datetime
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
