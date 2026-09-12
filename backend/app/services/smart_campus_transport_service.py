import uuid
from datetime import datetime
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.smart_campus_transport import (
    VehicleFuelLog,
    VehicleMaintenanceLog,
    HostelMaintenanceTicket,
)
from app.schemas.smart_campus_transport import (
    VehicleFuelLogCreate,
    VehicleMaintenanceLogCreate,
    HostelTicketCreate,
)


def log_vehicle_fuel(
    db: Session,
    filled_by_id: uuid.UUID,
    data: VehicleFuelLogCreate
) -> VehicleFuelLog:
    log = VehicleFuelLog(
        vehicle_id=data.vehicle_id,
        fuel_liters=data.fuel_liters,
        cost_amount=data.cost_amount,
        odometer_reading=data.odometer_reading,
        filled_by_id=filled_by_id,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def schedule_vehicle_maintenance(
    db: Session,
    data: VehicleMaintenanceLogCreate
) -> VehicleMaintenanceLog:
    maint = VehicleMaintenanceLog(
        vehicle_id=data.vehicle_id,
        service_type=data.service_type,
        description=data.description,
        cost_amount=data.cost_amount,
        scheduled_date=data.scheduled_date,
        status="SCHEDULED",
    )
    db.add(maint)
    db.commit()
    db.refresh(maint)
    return maint


def create_hostel_ticket(
    db: Session,
    data: HostelTicketCreate
) -> HostelMaintenanceTicket:
    ticket = HostelMaintenanceTicket(
        hostel_room_id=data.hostel_room_id,
        student_id=data.student_id,
        issue_category=data.issue_category,
        priority=data.priority,
        description=data.description,
        status="OPEN",
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
