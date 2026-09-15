from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HostelCreate(BaseModel):
    campus_id: UUID
    name: str
    type: str = "BOYS"
    capacity: int = 100
    warden_name: str | None = None


class HostelUpdate(BaseModel):
    campus_id: UUID | None = None
    name: str | None = None
    type: str | None = None
    capacity: int | None = None
    warden_name: str | None = None


class HostelResponse(BaseModel):
    id: UUID
    campus_id: UUID
    name: str
    type: str
    capacity: int
    warden_name: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
