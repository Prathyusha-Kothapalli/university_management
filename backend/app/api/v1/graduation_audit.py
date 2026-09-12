from uuid import uuid4
from typing import Dict, Any
from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/graduation-audit",
    tags=["Graduation Audit"]
)


class GraduationApplicationCreate(BaseModel):
    student_id: str
    program_id: str
    expected_graduation_term: str
    credits_completed: int
    cgpa: float


@router.post("/apply", status_code=status.HTTP_201_CREATED)
def apply_for_graduation(payload: GraduationApplicationCreate) -> Dict[str, Any]:
    return {
        "id": str(uuid4()),
        "student_id": payload.student_id,
        "program_id": payload.program_id,
        "expected_graduation_term": payload.expected_graduation_term,
        "credits_completed": payload.credits_completed,
        "cgpa": payload.cgpa,
        "status": "REQUIREMENTS_MET",
        "committee_approval": True
    }
