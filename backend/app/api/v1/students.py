from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.student import Student


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/")
def create_student(
    data: dict,
    db: Session = Depends(get_db)
):
    try:
        student = Student(**data)

        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):
    result = db.execute(select(Student))

    return result.scalars().all()


@router.get("/{student_id}")
def get_student(
    student_id: UUID,
    db: Session = Depends(get_db)
):
    student = db.get(Student, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}")
def update_student(
    student_id: UUID,
    data: dict,
    db: Session = Depends(get_db)
):
    student = db.get(Student, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    try:
        for key, value in data.items():
            if hasattr(student, key):
                setattr(student, key, value)

        db.commit()
        db.refresh(student)

        return student

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{student_id}")
def delete_student(
    student_id: UUID,
    db: Session = Depends(get_db)
):
    student = db.get(Student, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }