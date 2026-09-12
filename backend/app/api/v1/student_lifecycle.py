import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.student_lifecycle import (
    AcademicHoldCreate,
    AcademicHoldResponse,
    StudentConductCaseCreate,
    StudentConductCaseResponse,
    SupportCaseCreate,
    SupportCaseResponse,
)
from app.services import student_lifecycle_service

router = APIRouter(prefix="/student-lifecycle", tags=["Student Lifecycle"])


@router.post("/holds", response_model=AcademicHoldResponse, status_code=status.HTTP_201_CREATED)
def create_academic_hold(
    data: AcademicHoldCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Place an academic, financial, or administrative hold on a student profile."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return student_lifecycle_service.place_academic_hold(
        db=db,
        placed_by_id=user_id,
        hold_data=data,
    )


@router.put("/holds/{hold_id}/resolve", response_model=AcademicHoldResponse)
def resolve_hold(
    hold_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Resolve an active academic hold."""
    hold = student_lifecycle_service.resolve_academic_hold(db=db, hold_id=hold_id)
    if not hold:
        raise HTTPException(status_code=404, detail="Academic hold not found")
    return hold


@router.get("/holds/student/{student_id}", response_model=List[AcademicHoldResponse])
def list_student_holds(
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Fetch active academic holds for a student."""
    return student_lifecycle_service.get_active_student_holds(db=db, student_id=student_id)


@router.post("/conduct-cases", response_model=StudentConductCaseResponse, status_code=status.HTTP_201_CREATED)
def record_conduct_incident(
    data: StudentConductCaseCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Record a student conduct incident or disciplinary case."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return student_lifecycle_service.record_disciplinary_incident(
        db=db,
        reported_by_id=user_id,
        data=data,
    )


@router.post("/support-cases", response_model=SupportCaseResponse, status_code=status.HTTP_201_CREATED)
def submit_support_case(
    data: SupportCaseCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Open a new student advising or wellness support case."""
    return student_lifecycle_service.create_support_case(db=db, data=data)
