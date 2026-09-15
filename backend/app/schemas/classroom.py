from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ClassroomCreate(BaseModel):
    campus_id: UUID
    name: str
    code: str
    building: str | None = None
    floor: int | None = None
    capacity: int
    room_type: str = "CLASSROOM"
    is_active: bool = True


class ClassroomUpdate(BaseModel):
    campus_id: UUID | None = None
    name: str | None = None
    code: str | None = None
    building: str | None = None
    floor: int | None = None
    capacity: int | None = None
    room_type: str | None = None
    is_active: bool | None = None


class ClassroomResponse(BaseModel):
    id: UUID
    campus_id: UUID
    name: str
    code: str
    building: str | None
    floor: int | None
    capacity: int
    room_type: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)