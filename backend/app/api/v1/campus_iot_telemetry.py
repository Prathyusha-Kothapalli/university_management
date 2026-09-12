import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.campus_iot_telemetry import (
    IotDeviceCreate,
    IotDeviceResponse,
    TelemetryLogCreate,
    TelemetryLogResponse,
    SmartBuildingControlCreate,
    SmartBuildingControlResponse,
)
from app.services import campus_iot_telemetry_service

router = APIRouter(prefix="/campus-iot", tags=["Campus IoT & Smart Building Controls"])


@router.post("/devices", response_model=IotDeviceResponse, status_code=status.HTTP_201_CREATED)
def register_iot_device(
    data: IotDeviceCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Register smart IoT sensor or HVAC controller."""
    return campus_iot_telemetry_service.register_iot_device(
        db=db,
        data=data,
    )


@router.post("/telemetry", response_model=TelemetryLogResponse, status_code=status.HTTP_201_CREATED)
def log_telemetry_reading(
    data: TelemetryLogCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Log sensor metric telemetry reading (temperature, CO2, humidity, power)."""
    return campus_iot_telemetry_service.log_telemetry_reading(
        db=db,
        data=data,
    )


@router.post("/controls", response_model=SmartBuildingControlResponse, status_code=status.HTTP_201_CREATED)
def set_smart_building_control(
    data: SmartBuildingControlCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Adjust classroom HVAC target temperature, lighting level, and occupancy state."""
    return campus_iot_telemetry_service.set_building_control(
        db=db,
        data=data,
    )
