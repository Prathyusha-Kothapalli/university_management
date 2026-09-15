from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TransportRouteCreate(BaseModel):
    campus_id: UUID
    route_number: str
    route_name: str
    start_location: str
    end_location: str
    fee: float


class TransportRouteUpdate(BaseModel):
    campus_id: UUID | None = None
    route_number: str | None = None
    route_name: str | None = None
    start_location: str | None = None
    end_location: str | None = None
    fee: float | None = None


class TransportRouteResponse(BaseModel):
    id: UUID
    campus_id: UUID
    route_number: str
    route_name: str
    start_location: str
    end_location: str
    fee: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
