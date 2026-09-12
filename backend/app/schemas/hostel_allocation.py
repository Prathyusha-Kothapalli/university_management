from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HostelAllocationCreate(BaseModel):
    room_id: UUID
    student_id: UUID
    allocation_date: datetime | None = None
    vacate_date: datetime | None = None
    status: str = "ACTIVE"


class HostelAllocationUpdate(BaseModel):
    room_id: UUID | None = None
    student_id: UUID | None = None
    allocation_date: datetime | None = None
    vacate_date: datetime | None = None
    status: str | None = None


class HostelAllocationResponse(BaseModel):
    id: UUID
    room_id: UUID
    student_id: UUID
    allocation_date: datetime
    vacate_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
