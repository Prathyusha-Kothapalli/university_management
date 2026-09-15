from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.exam_result import ExamResult
from app.schemas.exam_result import (
    ExamResultCreate,
    ExamResultUpdate,
    ExamResultResponse,
)


router = APIRouter(
    prefix="/exam-results",
    tags=["Exam Results"]
)


@router.post(
    "/",
    response_model=ExamResultResponse
)
def create_exam_result(
    result_data: ExamResultCreate,
    db: Session = Depends(get_db)
):
    try:
        result_obj = ExamResult(
            **result_data.model_dump()
        )

        db.add(result_obj)
        db.commit()
        db.refresh(result_obj)

        return result_obj

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ExamResultResponse]
)
def get_exam_results(
    db: Session = Depends(get_db)
):
    query_result = db.execute(
        select(ExamResult)
    )

    return query_result.scalars().all()


@router.get(
    "/{result_id}",
    response_model=ExamResultResponse
)
def get_exam_result(
    result_id: UUID,
    db: Session = Depends(get_db)
):
    exam_result = db.get(
        ExamResult,
        result_id
    )

    if not exam_result:
        raise HTTPException(
            status_code=404,
            detail="Exam result not found"
        )

    return exam_result


@router.put(
    "/{result_id}",
    response_model=ExamResultResponse
)
def update_exam_result(
    result_id: UUID,
    result_data: ExamResultUpdate,
    db: Session = Depends(get_db)
):
    exam_result = db.get(
        ExamResult,
        result_id
    )

    if not exam_result:
        raise HTTPException(
            status_code=404,
            detail="Exam result not found"
        )

    try:
        update_data = result_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(exam_result, key):
                setattr(
                    exam_result,
                    key,
                    value
                )

        db.commit()
        db.refresh(exam_result)

        return exam_result

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{result_id}")
def delete_exam_result(
    result_id: UUID,
    db: Session = Depends(get_db)
):
    exam_result = db.get(
        ExamResult,
        result_id
    )

    if not exam_result:
        raise HTTPException(
            status_code=404,
            detail="Exam result not found"
        )

    db.delete(exam_result)
    db.commit()

    return {
        "message": "Exam result deleted successfully"
    }
