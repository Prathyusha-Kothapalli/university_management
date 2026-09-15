from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class CourseOutcomeCreate(BaseModel):
    code: str
    description: str
    bloom_taxonomy_level: str = "APPLY"
    target_attainment_pct: float = 75.0


class CourseOutcomeResponse(CourseOutcomeCreate):
    id: UUID
    course_offering_id: UUID

    class Config:
        from_attributes = True


class ProgramOutcomeCreate(BaseModel):
    code: str
    title: str
    description: str


class ProgramOutcomeResponse(ProgramOutcomeCreate):
    id: UUID
    program_id: UUID

    class Config:
        from_attributes = True


class CoPoMappingCreate(BaseModel):
    course_outcome_id: UUID
    program_outcome_id: UUID
    weight: int = Field(3, ge=1, le=3)


class CoPoMappingResponse(CoPoMappingCreate):
    id: UUID

    class Config:
        from_attributes = True


class WaitlistEntryResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    student_id: UUID
    position: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
