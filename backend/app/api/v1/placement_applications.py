from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.placement_application import PlacementApplication
from app.schemas.placement_application import (
    PlacementApplicationCreate,
    PlacementApplicationUpdate,
    PlacementApplicationResponse,
)


router = APIRouter(
    prefix="/placement-applications",
    tags=["Placement Applications"]
)


@router.post(
    "/",
    response_model=PlacementApplicationResponse
)
def create_placement_application(
    application_data: PlacementApplicationCreate,
    db: Session = Depends(get_db)
):
    try:
        application = PlacementApplication(
            **application_data.model_dump()
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[PlacementApplicationResponse]
)
def get_placement_applications(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(PlacementApplication)
    )

    return result.scalars().all()


@router.get(
    "/{application_id}",
    response_model=PlacementApplicationResponse
)
def get_placement_application(
    application_id: UUID,
    db: Session = Depends(get_db)
):
    application = db.get(
        PlacementApplication,
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Placement application not found"
        )

    return application


@router.put(
    "/{application_id}",
    response_model=PlacementApplicationResponse
)
def update_placement_application(
    application_id: UUID,
    application_data: PlacementApplicationUpdate,
    db: Session = Depends(get_db)
):
    application = db.get(
        PlacementApplication,
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Placement application not found"
        )

    try:
        update_data = application_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(application, key):
                setattr(
                    application,
                    key,
                    value
                )

        db.commit()
        db.refresh(application)

        return application

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{application_id}")
def delete_placement_application(
    application_id: UUID,
    db: Session = Depends(get_db)
):
    application = db.get(
        PlacementApplication,
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Placement application not found"
        )

    db.delete(application)
    db.commit()

    return {
        "message": "Placement application deleted successfully"
    }
