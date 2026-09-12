from pydantic import BaseModel
from typing import Optional, List

class ScholarshipBase(BaseModel):
    title: str
    sponsor: str
    amount_inr: float
    min_cgpa: float
    eligible_departments: List[str]
    deadline: str
    description: Optional[str] = None

class ScholarshipCreate(ScholarshipBase):
    pass

class Scholarship(ScholarshipBase):
    id: str
    available_grants: int
    status: str = "Active"

    class Config:
        from_attributes = True

class ScholarshipApplication(BaseModel):
    id: str
    scholarship_id: str
    student_id: str
    student_name: str
    cgpa: float
    applied_at: str
    status: str = "Under Review"

    class Config:
        from_attributes = True
