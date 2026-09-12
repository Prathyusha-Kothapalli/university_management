from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class IotDevice(Base):
    __tablename__ = "iot_devices"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    device_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    device_type: Mapped[str] = mapped_column(
        String(50), # TEMP_SENSOR, CO2_MONITOR, SMART_LOCK, HVAC_CONTROLLER
        nullable=False
    )

    classroom_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=True
    )

    mac_address: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    is_online: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


class IotTelemetryLog(Base):
    __tablename__ = "iot_telemetry_logs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    device_id: Mapped[UUID] = mapped_column(
        ForeignKey("iot_devices.id"),
        nullable=False,
        index=True
    )

    metric_name: Mapped[str] = mapped_column(
        String(50), # TEMPERATURE_C, CO2_PPM, HUMIDITY_PCT, POWER_WATTS
        nullable=False
    )

    metric_value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class SmartBuildingControl(Base):
    __tablename__ = "smart_building_controls"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    classroom_id: Mapped[UUID] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=False,
        index=True
    )

    target_temperature_c: Mapped[float] = mapped_column(
        Float,
        default=22.0
    )

    lighting_level_pct: Mapped[int] = mapped_column(
        Integer,
        default=80
    )

    is_occupied: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
