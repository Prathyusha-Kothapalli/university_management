from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.transport_vehicle import TransportVehicle
from app.schemas.transport_vehicle import (
    TransportVehicleCreate,
    TransportVehicleUpdate,
    TransportVehicleResponse,
)


router = APIRouter(
    prefix="/transport-vehicles",
    tags=["Transport Vehicles"]
)


@router.post(
    "/",
    response_model=TransportVehicleResponse
)
def create_transport_vehicle(
    vehicle_data: TransportVehicleCreate,
    db: Session = Depends(get_db)
):
    try:
        vehicle = TransportVehicle(
            **vehicle_data.model_dump()
        )

        db.add(vehicle)
        db.commit()
        db.refresh(vehicle)

        return vehicle

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[TransportVehicleResponse]
)
def get_transport_vehicles(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(TransportVehicle)
    )

    return result.scalars().all()


@router.get(
    "/{vehicle_id}",
    response_model=TransportVehicleResponse
)
def get_transport_vehicle(
    vehicle_id: UUID,
    db: Session = Depends(get_db)
):
    vehicle = db.get(
        TransportVehicle,
        vehicle_id
    )

    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail="Transport vehicle not found"
        )

    return vehicle


@router.put(
    "/{vehicle_id}",
    response_model=TransportVehicleResponse
)
def update_transport_vehicle(
    vehicle_id: UUID,
    vehicle_data: TransportVehicleUpdate,
    db: Session = Depends(get_db)
):
    vehicle = db.get(
        TransportVehicle,
        vehicle_id
    )

    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail="Transport vehicle not found"
        )

    try:
        update_data = vehicle_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(vehicle, key):
                setattr(
                    vehicle,
                    key,
                    value
                )

        db.commit()
        db.refresh(vehicle)

        return vehicle

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{vehicle_id}")
def delete_transport_vehicle(
    vehicle_id: UUID,
    db: Session = Depends(get_db)
):
    vehicle = db.get(
        TransportVehicle,
        vehicle_id
    )

    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail="Transport vehicle not found"
        )

    db.delete(vehicle)
    db.commit()

    return {
        "message": "Transport vehicle deleted successfully"
    }
