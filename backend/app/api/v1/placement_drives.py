from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.placement_drive import PlacementDrive
from app.schemas.placement_drive import (
    PlacementDriveCreate,
    PlacementDriveUpdate,
    PlacementDriveResponse,
)


router = APIRouter(
    prefix="/placement-drives",
    tags=["Placement Drives"]
)


@router.post(
    "/",
    response_model=PlacementDriveResponse
)
def create_placement_drive(
    drive_data: PlacementDriveCreate,
    db: Session = Depends(get_db)
):
    try:
        drive = PlacementDrive(
            **drive_data.model_dump()
        )

        db.add(drive)
        db.commit()
        db.refresh(drive)

        return drive

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[PlacementDriveResponse]
)
def get_placement_drives(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(PlacementDrive)
    )

    return result.scalars().all()


@router.get(
    "/{drive_id}",
    response_model=PlacementDriveResponse
)
def get_placement_drive(
    drive_id: UUID,
    db: Session = Depends(get_db)
):
    drive = db.get(
        PlacementDrive,
        drive_id
    )

    if not drive:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found"
        )

    return drive


@router.put(
    "/{drive_id}",
    response_model=PlacementDriveResponse
)
def update_placement_drive(
    drive_id: UUID,
    drive_data: PlacementDriveUpdate,
    db: Session = Depends(get_db)
):
    drive = db.get(
        PlacementDrive,
        drive_id
    )

    if not drive:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found"
        )

    try:
        update_data = drive_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(drive, key):
                setattr(
                    drive,
                    key,
                    value
                )

        db.commit()
        db.refresh(drive)

        return drive

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{drive_id}")
def delete_placement_drive(
    drive_id: UUID,
    db: Session = Depends(get_db)
):
    drive = db.get(
        PlacementDrive,
        drive_id
    )

    if not drive:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found"
        )

    db.delete(drive)
    db.commit()

    return {
        "message": "Placement drive deleted successfully"
    }
