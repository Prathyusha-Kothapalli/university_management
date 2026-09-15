import uuid
from datetime import datetime
from typing import List, Optional, Dict
from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.models.faculty_expansion import (
    FacultyQualification,
    FacultyAppraisal,
    ResearchProject,
    ResearchPublication,
)
from app.schemas.faculty_expansion import (
    FacultyQualificationCreate,
    FacultyAppraisalCreate,
    ResearchProjectCreate,
    ResearchPublicationCreate,
)


def add_faculty_qualification(
    db: Session,
    faculty_id: uuid.UUID,
    data: FacultyQualificationCreate
) -> FacultyQualification:
    qual = FacultyQualification(
        faculty_id=faculty_id,
        degree_name=data.degree_name,
        institution=data.institution,
        field_of_study=data.field_of_study,
        year_awarded=data.year_awarded,
        is_verified=True,
    )
    db.add(qual)
    db.commit()
    db.refresh(qual)
    return qual


def submit_faculty_appraisal(
    db: Session,
    faculty_id: uuid.UUID,
    data: FacultyAppraisalCreate
) -> FacultyAppraisal:
    overall = (
        data.teaching_score * 0.4 +
        data.research_score * 0.4 +
        data.service_score * 0.2
    )
    appraisal = FacultyAppraisal(
        faculty_id=faculty_id,
        academic_year_id=data.academic_year_id,
        teaching_score=data.teaching_score,
        research_score=data.research_score,
        service_score=data.service_score,
        overall_rating=overall,
        self_assessment=data.self_assessment,
        reviewer_comments=data.reviewer_comments,
        status="SUBMITTED",
    )
    db.add(appraisal)
    db.commit()
    db.refresh(appraisal)
    return appraisal


def create_research_project(
    db: Session,
    lead_faculty_id: uuid.UUID,
    data: ResearchProjectCreate
) -> ResearchProject:
    project = ResearchProject(
        lead_faculty_id=lead_faculty_id,
        title=data.title,
        grant_agency=data.grant_agency,
        grant_amount=data.grant_amount,
        status=data.status,
        start_date=data.start_date,
        end_date=data.end_date,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def index_research_publication(
    db: Session,
    faculty_id: uuid.UUID,
    data: ResearchPublicationCreate
) -> ResearchPublication:
    pub = ResearchPublication(
        faculty_id=faculty_id,
        title=data.title,
        journal_conference=data.journal_conference,
        doi=data.doi,
        publication_date=data.publication_date,
        citation_count=data.citation_count,
        impact_factor=data.impact_factor,
        is_peer_reviewed=data.is_peer_reviewed,
    )
    db.add(pub)
    db.commit()
    db.refresh(pub)
    return pub


def get_faculty_workload_metrics(db: Session, faculty_id: uuid.UUID) -> Dict[str, float]:
    quals = db.execute(
        select(func.count(FacultyQualification.id)).where(FacultyQualification.faculty_id == faculty_id)
    ).scalar() or 0

    pubs = db.execute(
        select(func.count(ResearchPublication.id)).where(ResearchPublication.faculty_id == faculty_id)
    ).scalar() or 0

    projects = db.execute(
        select(func.sum(ResearchProject.grant_amount)).where(ResearchProject.lead_faculty_id == faculty_id)
    ).scalar() or 0.0

    return {
        "qualification_count": float(quals),
        "publication_count": float(pubs),
        "total_grant_funding": float(projects),
    }
