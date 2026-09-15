from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.classroom import Classroom
from app.schemas.classroom import (
    ClassroomCreate,
    ClassroomUpdate,
    ClassroomResponse,
)


router = APIRouter(
    prefix="/classrooms",
    tags=["Classrooms"]
)


@router.post(
    "/",
    response_model=ClassroomResponse
)
def create_classroom(
    classroom_data: ClassroomCreate,
    db: Session = Depends(get_db)
):
    try:
        classroom = Classroom(
            **classroom_data.model_dump()
        )

        db.add(classroom)
        db.commit()
        db.refresh(classroom)

        return classroom

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ClassroomResponse]
)
def get_classrooms(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Classroom)
    )

    return result.scalars().all()


@router.get(
    "/{classroom_id}",
    response_model=ClassroomResponse
)
def get_classroom(
    classroom_id: UUID,
    db: Session = Depends(get_db)
):
    classroom = db.get(
        Classroom,
        classroom_id
    )

    if not classroom:
        raise HTTPException(
            status_code=404,
            detail="Classroom not found"
        )

    return classroom


@router.put(
    "/{classroom_id}",
    response_model=ClassroomResponse
)
def update_classroom(
    classroom_id: UUID,
    classroom_data: ClassroomUpdate,
    db: Session = Depends(get_db)
):
    classroom = db.get(
        Classroom,
        classroom_id
    )

    if not classroom:
        raise HTTPException(
            status_code=404,
            detail="Classroom not found"
        )

    try:
        update_data = classroom_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(classroom, key):
                setattr(
                    classroom,
                    key,
                    value
                )

        db.commit()
        db.refresh(classroom)

        return classroom

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{classroom_id}")
def delete_classroom(
    classroom_id: UUID,
    db: Session = Depends(get_db)
):
    classroom = db.get(
        Classroom,
        classroom_id
    )

    if not classroom:
        raise HTTPException(
            status_code=404,
            detail="Classroom not found"
        )

    db.delete(classroom)
    db.commit()

    return {
        "message": "Classroom deleted successfully"
    }