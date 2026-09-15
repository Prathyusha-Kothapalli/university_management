from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HostelRoomCreate(BaseModel):
    hostel_id: UUID
    room_number: str
    floor: int = 1
    capacity: int = 2
    occupied_count: int = 0
    monthly_fee: float


class HostelRoomUpdate(BaseModel):
    hostel_id: UUID | None = None
    room_number: str | None = None
    floor: int | None = None
    capacity: int | None = None
    occupied_count: int | None = None
    monthly_fee: float | None = None


class HostelRoomResponse(BaseModel):
    id: UUID
    hostel_id: UUID
    room_number: str
    floor: int
    capacity: int
    occupied_count: int
    monthly_fee: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
