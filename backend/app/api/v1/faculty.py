from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.faculty import Faculty


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)


@router.post("/")
def create_faculty(
    data: dict,
    db: Session = Depends(get_db)
):
    try:
        faculty = Faculty(**data)

        db.add(faculty)
        db.commit()
        db.refresh(faculty)

        return faculty

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/")
def get_faculty(
    db: Session = Depends(get_db)
):
    result = db.execute(select(Faculty))

    return result.scalars().all()


@router.get("/{faculty_id}")
def get_faculty_member(
    faculty_id: UUID,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    return faculty


@router.put("/{faculty_id}")
def update_faculty(
    faculty_id: UUID,
    data: dict,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    try:
        for key, value in data.items():
            if hasattr(faculty, key):
                setattr(faculty, key, value)

        db.commit()
        db.refresh(faculty)

        return faculty

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{faculty_id}")
def delete_faculty(
    faculty_id: UUID,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    db.delete(faculty)
    db.commit()

    return {
        "message": "Faculty member deleted successfully"
    }