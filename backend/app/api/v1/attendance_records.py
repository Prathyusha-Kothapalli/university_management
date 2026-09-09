from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.attendance_record import AttendanceRecord
from app.schemas.attendance_record import (
    AttendanceRecordCreate,
    AttendanceRecordUpdate,
    AttendanceRecordResponse,
)


router = APIRouter(
    prefix="/attendance-records",
    tags=["Attendance Records"]
)


@router.post(
    "/",
    response_model=AttendanceRecordResponse
)
def create_attendance_record(
    record_data: AttendanceRecordCreate,
    db: Session = Depends(get_db)
):
    try:
        attendance_record = AttendanceRecord(
            **record_data.model_dump()
        )

        db.add(attendance_record)
        db.commit()
        db.refresh(attendance_record)

        return attendance_record

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AttendanceRecordResponse]
)
def get_attendance_records(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AttendanceRecord)
    )

    return result.scalars().all()


@router.get(
    "/{record_id}",
    response_model=AttendanceRecordResponse
)
def get_attendance_record(
    record_id: UUID,
    db: Session = Depends(get_db)
):
    attendance_record = db.get(
        AttendanceRecord,
        record_id
    )

    if not attendance_record:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance_record


@router.put(
    "/{record_id}",
    response_model=AttendanceRecordResponse
)
def update_attendance_record(
    record_id: UUID,
    record_data: AttendanceRecordUpdate,
    db: Session = Depends(get_db)
):
    attendance_record = db.get(
        AttendanceRecord,
        record_id
    )

    if not attendance_record:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    try:
        update_data = record_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(attendance_record, key):
                setattr(
                    attendance_record,
                    key,
                    value
                )

        db.commit()
        db.refresh(attendance_record)

        return attendance_record

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{record_id}")
def delete_attendance_record(
    record_id: UUID,
    db: Session = Depends(get_db)
):
    attendance_record = db.get(
        AttendanceRecord,
        record_id
    )

    if not attendance_record:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    db.delete(attendance_record)
    db.commit()

    return {
        "message": "Attendance record deleted successfully"
    }