from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.timetable import Timetable
from app.schemas.timetable import (
    TimetableCreate,
    TimetableUpdate,
    TimetableResponse,
)


router = APIRouter(
    prefix="/timetables",
    tags=["Timetables"]
)


@router.post(
    "/",
    response_model=TimetableResponse
)
def create_timetable(
    timetable_data: TimetableCreate,
    db: Session = Depends(get_db)
):
    try:
        timetable = Timetable(
            **timetable_data.model_dump()
        )

        db.add(timetable)
        db.commit()
        db.refresh(timetable)

        return timetable

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[TimetableResponse]
)
def get_timetables(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Timetable)
    )

    return result.scalars().all()


@router.get(
    "/{timetable_id}",
    response_model=TimetableResponse
)
def get_timetable(
    timetable_id: UUID,
    db: Session = Depends(get_db)
):
    timetable = db.get(
        Timetable,
        timetable_id
    )

    if not timetable:
        raise HTTPException(
            status_code=404,
            detail="Timetable not found"
        )

    return timetable


@router.put(
    "/{timetable_id}",
    response_model=TimetableResponse
)
def update_timetable(
    timetable_id: UUID,
    timetable_data: TimetableUpdate,
    db: Session = Depends(get_db)
):
    timetable = db.get(
        Timetable,
        timetable_id
    )

    if not timetable:
        raise HTTPException(
            status_code=404,
            detail="Timetable not found"
        )

    try:
        update_data = timetable_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(timetable, key):
                setattr(
                    timetable,
                    key,
                    value
                )

        db.commit()
        db.refresh(timetable)

        return timetable

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{timetable_id}")
def delete_timetable(
    timetable_id: UUID,
    db: Session = Depends(get_db)
):
    timetable = db.get(
        Timetable,
        timetable_id
    )

    if not timetable:
        raise HTTPException(
            status_code=404,
            detail="Timetable not found"
        )

    db.delete(timetable)
    db.commit()

    return {
        "message": "Timetable deleted successfully"
    }