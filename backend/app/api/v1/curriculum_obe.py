import uuid
from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.curriculum_obe import (
    CourseOutcomeCreate,
    CourseOutcomeResponse,
    ProgramOutcomeCreate,
    ProgramOutcomeResponse,
    CoPoMappingCreate,
    CoPoMappingResponse,
    WaitlistEntryResponse,
)
from app.services import curriculum_obe_service

router = APIRouter(prefix="/curriculum-obe", tags=["Curriculum & OBE"])


@router.post("/course-outcomes/{offering_id}", response_model=CourseOutcomeResponse, status_code=status.HTTP_201_CREATED)
def add_course_outcome(
    offering_id: uuid.UUID,
    data: CourseOutcomeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Add a Course Outcome (CO) tied to a course offering."""
    return curriculum_obe_service.create_course_outcome(
        db=db,
        offering_id=offering_id,
        data=data,
    )


@router.post("/program-outcomes/{program_id}", response_model=ProgramOutcomeResponse, status_code=status.HTTP_201_CREATED)
def add_program_outcome(
    program_id: uuid.UUID,
    data: ProgramOutcomeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Add a Program Outcome (PO) tied to an academic degree program."""
    return curriculum_obe_service.create_program_outcome(
        db=db,
        program_id=program_id,
        data=data,
    )


@router.post("/mappings", response_model=CoPoMappingResponse, status_code=status.HTTP_201_CREATED)
def map_co_po(
    data: CoPoMappingCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Map a Course Outcome to a Program Outcome with a weighted contribution score."""
    return curriculum_obe_service.map_co_to_po(
        db=db,
        data=data,
    )


@router.get("/attainment-matrix/{offering_id}", response_model=List[Dict])
def get_attainment_matrix(
    offering_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Fetch the calculated Outcome-Based Education (OBE) CO-PO attainment matrix."""
    return curriculum_obe_service.calculate_attainment_matrix(
        db=db,
        offering_id=offering_id,
    )


@router.post("/waitlist/{offering_id}", response_model=WaitlistEntryResponse, status_code=status.HTTP_201_CREATED)
def join_waitlist(
    offering_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Join the course enrollment waitlist."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return curriculum_obe_service.join_course_waitlist(
        db=db,
        student_id=user_id,
        offering_id=offering_id,
    )
