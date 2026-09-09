from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.attendance_session import AttendanceSession
from app.schemas.attendance_session import (
    AttendanceSessionCreate,
    AttendanceSessionUpdate,
    AttendanceSessionResponse,
)


router = APIRouter(
    prefix="/attendance-sessions",
    tags=["Attendance Sessions"]
)


@router.post(
    "/",
    response_model=AttendanceSessionResponse
)
def create_attendance_session(
    session_data: AttendanceSessionCreate,
    db: Session = Depends(get_db)
):
    try:
        attendance_session = AttendanceSession(
            **session_data.model_dump()
        )

        db.add(attendance_session)
        db.commit()
        db.refresh(attendance_session)

        return attendance_session

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AttendanceSessionResponse]
)
def get_attendance_sessions(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AttendanceSession)
    )

    return result.scalars().all()


@router.get(
    "/{session_id}",
    response_model=AttendanceSessionResponse
)
def get_attendance_session(
    session_id: UUID,
    db: Session = Depends(get_db)
):
    attendance_session = db.get(
        AttendanceSession,
        session_id
    )

    if not attendance_session:
        raise HTTPException(
            status_code=404,
            detail="Attendance session not found"
        )

    return attendance_session


@router.put(
    "/{session_id}",
    response_model=AttendanceSessionResponse
)
def update_attendance_session(
    session_id: UUID,
    session_data: AttendanceSessionUpdate,
    db: Session = Depends(get_db)
):
    attendance_session = db.get(
        AttendanceSession,
        session_id
    )

    if not attendance_session:
        raise HTTPException(
            status_code=404,
            detail="Attendance session not found"
        )

    try:
        update_data = session_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(attendance_session, key):
                setattr(
                    attendance_session,
                    key,
                    value
                )

        db.commit()
        db.refresh(attendance_session)

        return attendance_session

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{session_id}")
def delete_attendance_session(
    session_id: UUID,
    db: Session = Depends(get_db)
):
    attendance_session = db.get(
        AttendanceSession,
        session_id
    )

    if not attendance_session:
        raise HTTPException(
            status_code=404,
            detail="Attendance session not found"
        )

    db.delete(attendance_session)
    db.commit()

    return {
        "message": "Attendance session deleted successfully"
    }