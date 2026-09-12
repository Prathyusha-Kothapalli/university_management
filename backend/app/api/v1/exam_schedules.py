from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.exam_schedule import ExamSchedule
from app.schemas.exam_schedule import (
    ExamScheduleCreate,
    ExamScheduleUpdate,
    ExamScheduleResponse,
)


router = APIRouter(
    prefix="/exam-schedules",
    tags=["Exam Schedules"]
)


@router.post(
    "/",
    response_model=ExamScheduleResponse
)
def create_exam_schedule(
    schedule_data: ExamScheduleCreate,
    db: Session = Depends(get_db)
):
    try:
        schedule = ExamSchedule(
            **schedule_data.model_dump()
        )

        db.add(schedule)
        db.commit()
        db.refresh(schedule)

        return schedule

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ExamScheduleResponse]
)
def get_exam_schedules(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(ExamSchedule)
    )

    return result.scalars().all()


@router.get(
    "/{schedule_id}",
    response_model=ExamScheduleResponse
)
def get_exam_schedule(
    schedule_id: UUID,
    db: Session = Depends(get_db)
):
    schedule = db.get(
        ExamSchedule,
        schedule_id
    )

    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Exam schedule not found"
        )

    return schedule


@router.put(
    "/{schedule_id}",
    response_model=ExamScheduleResponse
)
def update_exam_schedule(
    schedule_id: UUID,
    schedule_data: ExamScheduleUpdate,
    db: Session = Depends(get_db)
):
    schedule = db.get(
        ExamSchedule,
        schedule_id
    )

    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Exam schedule not found"
        )

    try:
        update_data = schedule_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(schedule, key):
                setattr(
                    schedule,
                    key,
                    value
                )

        db.commit()
        db.refresh(schedule)

        return schedule

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{schedule_id}")
def delete_exam_schedule(
    schedule_id: UUID,
    db: Session = Depends(get_db)
):
    schedule = db.get(
        ExamSchedule,
        schedule_id
    )

    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Exam schedule not found"
        )

    db.delete(schedule)
    db.commit()

    return {
        "message": "Exam schedule deleted successfully"
    }
