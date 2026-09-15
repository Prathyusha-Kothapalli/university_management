from uuid import UUID
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.attendance_record import AttendanceRecord
from app.models.attendance_exemption import AttendanceExemption
from app.schemas.attendance_record import (
    AttendanceRecordCreate,
    AttendanceRecordUpdate,
    AttendanceRecordResponse,
)
from app.services.attendance_service import (
    generate_qr_attendance_token,
    validate_qr_attendance_scan,
)


class QrScanRequest(BaseModel):
    qr_payload: str
    student_id: UUID


class ExemptionRequestSchema(BaseModel):
    student_id: UUID
    course_id: UUID
    exemption_type: str
    start_date: str
    end_date: str
    reason: str


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


@router.get("/qr/generate/{session_id}")
def generate_qr_token(session_id: UUID):
    token = generate_qr_attendance_token(session_id)
    return {
        "session_id": str(session_id),
        "qr_token": token,
        "expires_in_seconds": 60
    }


@router.post("/qr/scan")
def scan_qr_token(data: QrScanRequest, db: Session = Depends(get_db)):
    result = validate_qr_attendance_scan(data.qr_payload, data.student_id, db)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result


@router.post("/exemptions")
def create_exemption_request(data: ExemptionRequestSchema, db: Session = Depends(get_db)):
    try:
        s_date = datetime.fromisoformat(data.start_date.replace("Z", "+00:00"))
        e_date = datetime.fromisoformat(data.end_date.replace("Z", "+00:00"))
    except Exception:
        s_date = datetime.utcnow()
        e_date = datetime.utcnow()

    exemption = AttendanceExemption(
        student_id=data.student_id,
        course_id=data.course_id,
        exemption_type=data.exemption_type,
        start_date=s_date,
        end_date=e_date,
        reason=data.reason,
        status="PENDING"
    )
    db.add(exemption)
    db.commit()
    db.refresh(exemption)
    return {"message": "Attendance exemption submitted for review", "exemption_id": str(exemption.id)}


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