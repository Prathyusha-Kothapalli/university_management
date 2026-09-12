from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TransportVehicleCreate(BaseModel):
    route_id: UUID
    vehicle_number: str
    capacity: int = 40
    driver_name: str | None = None
    driver_phone: str | None = None


class TransportVehicleUpdate(BaseModel):
    route_id: UUID | None = None
    vehicle_number: str | None = None
    capacity: int | None = None
    driver_name: str | None = None
    driver_phone: str | None = None


class TransportVehicleResponse(BaseModel):
    id: UUID
    route_id: UUID
    vehicle_number: str
    capacity: int
    driver_name: str | None
    driver_phone: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
