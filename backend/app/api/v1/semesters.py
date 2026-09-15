from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.semester import Semester
from app.schemas.semester import (
    SemesterCreate,
    SemesterUpdate,
    SemesterResponse,
)


router = APIRouter(
    prefix="/semesters",
    tags=["Semesters"]
)


@router.post(
    "/",
    response_model=SemesterResponse
)
def create_semester(
    semester_data: SemesterCreate,
    db: Session = Depends(get_db)
):
    try:
        semester = Semester(
            **semester_data.model_dump()
        )

        db.add(semester)
        db.commit()
        db.refresh(semester)

        return semester

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[SemesterResponse]
)
def get_semesters(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Semester)
    )

    return result.scalars().all()


@router.get(
    "/{semester_id}",
    response_model=SemesterResponse
)
def get_semester(
    semester_id: UUID,
    db: Session = Depends(get_db)
):
    semester = db.get(
        Semester,
        semester_id
    )

    if not semester:
        raise HTTPException(
            status_code=404,
            detail="Semester not found"
        )

    return semester


@router.put(
    "/{semester_id}",
    response_model=SemesterResponse
)
def update_semester(
    semester_id: UUID,
    semester_data: SemesterUpdate,
    db: Session = Depends(get_db)
):
    semester = db.get(
        Semester,
        semester_id
    )

    if not semester:
        raise HTTPException(
            status_code=404,
            detail="Semester not found"
        )

    try:
        update_data = semester_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(semester, key):
                setattr(
                    semester,
                    key,
                    value
                )

        db.commit()
        db.refresh(semester)

        return semester

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{semester_id}")
def delete_semester(
    semester_id: UUID,
    db: Session = Depends(get_db)
):
    semester = db.get(
        Semester,
        semester_id
    )

    if not semester:
        raise HTTPException(
            status_code=404,
            detail="Semester not found"
        )

    db.delete(semester)
    db.commit()

    return {
        "message": "Semester deleted successfully"
    }