from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TransportAllocationCreate(BaseModel):
    route_id: UUID
    student_id: UUID
    stop_location: str
    start_date: datetime | None = None
    end_date: datetime | None = None
    status: str = "ACTIVE"


class TransportAllocationUpdate(BaseModel):
    route_id: UUID | None = None
    student_id: UUID | None = None
    stop_location: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    status: str | None = None


class TransportAllocationResponse(BaseModel):
    id: UUID
    route_id: UUID
    student_id: UUID
    stop_location: str
    start_date: datetime
    end_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
