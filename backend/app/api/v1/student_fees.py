from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.student_fee import StudentFee
from app.schemas.student_fee import (
    StudentFeeCreate,
    StudentFeeUpdate,
    StudentFeeResponse,
)


router = APIRouter(
    prefix="/student-fees",
    tags=["Student Fees"]
)


@router.post(
    "/",
    response_model=StudentFeeResponse
)
def create_student_fee(
    fee_data: StudentFeeCreate,
    db: Session = Depends(get_db)
):
    try:
        student_fee = StudentFee(
            **fee_data.model_dump()
        )

        db.add(student_fee)
        db.commit()
        db.refresh(student_fee)

        return student_fee

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[StudentFeeResponse]
)
def get_student_fees(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(StudentFee)
    )

    return result.scalars().all()


@router.get(
    "/{student_fee_id}",
    response_model=StudentFeeResponse
)
def get_student_fee(
    student_fee_id: UUID,
    db: Session = Depends(get_db)
):
    student_fee = db.get(
        StudentFee,
        student_fee_id
    )

    if not student_fee:
        raise HTTPException(
            status_code=404,
            detail="Student fee not found"
        )

    return student_fee


@router.put(
    "/{student_fee_id}",
    response_model=StudentFeeResponse
)
def update_student_fee(
    student_fee_id: UUID,
    fee_data: StudentFeeUpdate,
    db: Session = Depends(get_db)
):
    student_fee = db.get(
        StudentFee,
        student_fee_id
    )

    if not student_fee:
        raise HTTPException(
            status_code=404,
            detail="Student fee not found"
        )

    try:
        update_data = fee_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(student_fee, key):
                setattr(
                    student_fee,
                    key,
                    value
                )

        db.commit()
        db.refresh(student_fee)

        return student_fee

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{student_fee_id}")
def delete_student_fee(
    student_fee_id: UUID,
    db: Session = Depends(get_db)
):
    student_fee = db.get(
        StudentFee,
        student_fee_id
    )

    if not student_fee:
        raise HTTPException(
            status_code=404,
            detail="Student fee not found"
        )

    db.delete(student_fee)
    db.commit()

    return {
        "message": "Student fee deleted successfully"
    }
