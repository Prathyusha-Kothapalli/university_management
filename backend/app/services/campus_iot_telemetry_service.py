import uuid
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.campus_iot_telemetry import (
    IotDevice,
    IotTelemetryLog,
    SmartBuildingControl,
)
from app.schemas.campus_iot_telemetry import (
    IotDeviceCreate,
    TelemetryLogCreate,
    SmartBuildingControlCreate,
)


def register_iot_device(
    db: Session,
    data: IotDeviceCreate
) -> IotDevice:
    device = IotDevice(
        device_name=data.device_name,
        device_type=data.device_type,
        classroom_id=data.classroom_id,
        mac_address=data.mac_address,
        is_online=True,
    )
    db.add(device)
    db.commit()
    db.refresh(device)
    return device


def log_telemetry_reading(
    db: Session,
    data: TelemetryLogCreate
) -> IotTelemetryLog:
    log = IotTelemetryLog(
        device_id=data.device_id,
        metric_name=data.metric_name,
        metric_value=data.metric_value,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def set_building_control(
    db: Session,
    data: SmartBuildingControlCreate
) -> SmartBuildingControl:
    control = db.execute(
        select(SmartBuildingControl).where(SmartBuildingControl.classroom_id == data.classroom_id)
    ).scalar_one_or_none()

    if control:
        control.target_temperature_c = data.target_temperature_c
        control.lighting_level_pct = data.lighting_level_pct
        control.is_occupied = data.is_occupied
        db.commit()
        db.refresh(control)
        return control

    control = SmartBuildingControl(
        classroom_id=data.classroom_id,
        target_temperature_c=data.target_temperature_c,
        lighting_level_pct=data.lighting_level_pct,
        is_occupied=data.is_occupied,
    )
    db.add(control)
    db.commit()
    db.refresh(control)
    return control
