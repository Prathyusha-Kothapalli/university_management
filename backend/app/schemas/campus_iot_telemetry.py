from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class IotDeviceCreate(BaseModel):
    device_name: str
    device_type: str # TEMP_SENSOR, CO2_MONITOR, SMART_LOCK
    classroom_id: Optional[UUID] = None
    mac_address: str


class IotDeviceResponse(IotDeviceCreate):
    id: UUID
    is_online: bool

    class Config:
        from_attributes = True


class TelemetryLogCreate(BaseModel):
    device_id: UUID
    metric_name: str
    metric_value: float


class TelemetryLogResponse(TelemetryLogCreate):
    id: UUID
    logged_at: datetime

    class Config:
        from_attributes = True


class SmartBuildingControlCreate(BaseModel):
    classroom_id: UUID
    target_temperature_c: float = 22.0
    lighting_level_pct: int = 80
    is_occupied: bool = False


class SmartBuildingControlResponse(SmartBuildingControlCreate):
    id: UUID

    class Config:
        from_attributes = True
