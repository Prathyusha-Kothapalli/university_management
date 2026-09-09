from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.campus import Campus
from app.schemas.campus import (
    CampusCreate,
    CampusUpdate,
    CampusResponse,
)


router = APIRouter(
    prefix="/campuses",
    tags=["Campuses"]
)


@router.post(
    "/",
    response_model=CampusResponse
)
def create_campus(
    campus_data: CampusCreate,
    db: Session = Depends(get_db)
):
    try:
        campus = Campus(
            **campus_data.model_dump()
        )

        db.add(campus)
        db.commit()
        db.refresh(campus)

        return campus

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CampusResponse]
)
def get_campuses(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Campus)
    )

    return result.scalars().all()


@router.get(
    "/{campus_id}",
    response_model=CampusResponse
)
def get_campus(
    campus_id: UUID,
    db: Session = Depends(get_db)
):
    campus = db.get(Campus, campus_id)

    if not campus:
        raise HTTPException(
            status_code=404,
            detail="Campus not found"
        )

    return campus


@router.put(
    "/{campus_id}",
    response_model=CampusResponse
)
def update_campus(
    campus_id: UUID,
    campus_data: CampusUpdate,
    db: Session = Depends(get_db)
):
    campus = db.get(Campus, campus_id)

    if not campus:
        raise HTTPException(
            status_code=404,
            detail="Campus not found"
        )

    try:
        update_data = campus_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(campus, key):
                setattr(campus, key, value)

        db.commit()
        db.refresh(campus)

        return campus

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{campus_id}")
def delete_campus(
    campus_id: UUID,
    db: Session = Depends(get_db)
):
    campus = db.get(Campus, campus_id)

    if not campus:
        raise HTTPException(
            status_code=404,
            detail="Campus not found"
        )

    db.delete(campus)
    db.commit()

    return {
        "message": "Campus deleted successfully"
    }