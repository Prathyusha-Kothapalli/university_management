import uuid
from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.faculty_expansion import (
    FacultyQualificationCreate,
    FacultyQualificationResponse,
    FacultyAppraisalCreate,
    FacultyAppraisalResponse,
    ResearchProjectCreate,
    ResearchProjectResponse,
    ResearchPublicationCreate,
    ResearchPublicationResponse,
)
from app.services import faculty_expansion_service

router = APIRouter(prefix="/faculty-expansion", tags=["Faculty Expansion"])


@router.post("/qualifications", response_model=FacultyQualificationResponse, status_code=status.HTTP_201_CREATED)
def add_qualification(
    faculty_id: uuid.UUID,
    data: FacultyQualificationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Add academic degree qualification to faculty record."""
    return faculty_expansion_service.add_faculty_qualification(
        db=db,
        faculty_id=faculty_id,
        data=data,
    )


@router.post("/appraisals", response_model=FacultyAppraisalResponse, status_code=status.HTTP_201_CREATED)
def submit_appraisal(
    faculty_id: uuid.UUID,
    data: FacultyAppraisalCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Submit annual performance appraisal for faculty member."""
    return faculty_expansion_service.submit_faculty_appraisal(
        db=db,
        faculty_id=faculty_id,
        data=data,
    )


@router.post("/research-projects", response_model=ResearchProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    data: ResearchProjectCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Register funded research project."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return faculty_expansion_service.create_research_project(
        db=db,
        lead_faculty_id=user_id,
        data=data,
    )


@router.post("/publications", response_model=ResearchPublicationResponse, status_code=status.HTTP_201_CREATED)
def index_publication(
    faculty_id: uuid.UUID,
    data: ResearchPublicationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Index peer-reviewed publication or conference paper."""
    return faculty_expansion_service.index_research_publication(
        db=db,
        faculty_id=faculty_id,
        data=data,
    )


@router.get("/metrics/{faculty_id}", response_model=Dict[str, float])
def get_metrics(
    faculty_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get summarized research, qualification, and workload metrics."""
    return faculty_expansion_service.get_faculty_workload_metrics(
        db=db,
        faculty_id=faculty_id,
    )
