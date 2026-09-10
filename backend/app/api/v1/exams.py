from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.exam import Exam
from app.schemas.exam import (
    ExamCreate,
    ExamUpdate,
    ExamResponse,
)


router = APIRouter(
    prefix="/exams",
    tags=["Exams"]
)


@router.post(
    "/",
    response_model=ExamResponse
)
def create_exam(
    exam_data: ExamCreate,
    db: Session = Depends(get_db)
):
    try:
        exam = Exam(
            **exam_data.model_dump()
        )

        db.add(exam)
        db.commit()
        db.refresh(exam)

        return exam

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ExamResponse]
)
def get_exams(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Exam)
    )

    return result.scalars().all()


@router.get(
    "/{exam_id}",
    response_model=ExamResponse
)
def get_exam(
    exam_id: UUID,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    return exam


@router.put(
    "/{exam_id}",
    response_model=ExamResponse
)
def update_exam(
    exam_id: UUID,
    exam_data: ExamUpdate,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    try:
        update_data = exam_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(exam, key):
                setattr(
                    exam,
                    key,
                    value
                )

        db.commit()
        db.refresh(exam)

        return exam

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{exam_id}")
def delete_exam(
    exam_id: UUID,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    db.delete(exam)
    db.commit()

    return {
        "message": "Exam deleted successfully"
    }
