import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.smart_campus_transport import (
    VehicleFuelLogCreate,
    VehicleFuelLogResponse,
    VehicleMaintenanceLogCreate,
    VehicleMaintenanceLogResponse,
    HostelTicketCreate,
    HostelTicketResponse,
)
from app.services import smart_campus_transport_service

router = APIRouter(prefix="/campus-transport", tags=["Smart Campus Transport & Hostel"])


@router.post("/fuel-logs", response_model=VehicleFuelLogResponse, status_code=status.HTTP_201_CREATED)
def log_vehicle_fuel(
    data: VehicleFuelLogCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Log fuel fill expense and odometer reading for fleet vehicle."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return smart_campus_transport_service.log_vehicle_fuel(
        db=db,
        filled_by_id=user_id,
        data=data,
    )


@router.post("/maintenance-logs", response_model=VehicleMaintenanceLogResponse, status_code=status.HTTP_201_CREATED)
def schedule_vehicle_maintenance(
    data: VehicleMaintenanceLogCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Schedule maintenance or overhaul for campus bus/van."""
    return smart_campus_transport_service.schedule_vehicle_maintenance(
        db=db,
        data=data,
    )


@router.post("/hostel-tickets", response_model=HostelTicketResponse, status_code=status.HTTP_201_CREATED)
def submit_hostel_ticket(
    data: HostelTicketCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create hostel room maintenance ticket."""
    return smart_campus_transport_service.create_hostel_ticket(
        db=db,
        data=data,
    )
