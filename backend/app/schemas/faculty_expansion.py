from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class FacultyQualificationCreate(BaseModel):
    degree_name: str
    field_of_study: str
    institution: str
    year_awarded: int


class FacultyQualificationResponse(FacultyQualificationCreate):
    id: UUID
    faculty_id: UUID
    is_verified: bool

    class Config:
        from_attributes = True


class FacultyAppraisalCreate(BaseModel):
    academic_year_id: UUID
    teaching_score: float = 4.0
    research_score: float = 4.0
    service_score: float = 4.0
    self_assessment: str = ""
    reviewer_comments: str = ""


class FacultyAppraisalResponse(FacultyAppraisalCreate):
    id: UUID
    faculty_id: UUID
    overall_rating: float
    status: str

    class Config:
        from_attributes = True


class ResearchProjectCreate(BaseModel):
    title: str
    grant_agency: str = "National Science Foundation"
    grant_amount: float = 50000.0
    status: str = "ACTIVE"
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: Optional[datetime] = None


class ResearchProjectResponse(ResearchProjectCreate):
    id: UUID
    lead_faculty_id: UUID

    class Config:
        from_attributes = True


class ResearchPublicationCreate(BaseModel):
    title: str
    journal_conference: str
    doi: Optional[str] = None
    publication_date: datetime = Field(default_factory=datetime.utcnow)
    citation_count: int = 0
    impact_factor: float = 2.5
    is_peer_reviewed: bool = True


class ResearchPublicationResponse(ResearchPublicationCreate):
    id: UUID
    faculty_id: UUID

    class Config:
        from_attributes = True
