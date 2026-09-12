from uuid import uuid4
from typing import List, Dict, Any
from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/academic-advising",
    tags=["Academic Advising"]
)

_assignments_db: List[Dict[str, Any]] = []
_interventions_db: List[Dict[str, Any]] = []


class InterventionCreate(BaseModel):
    student_id: str
    risk_level: str
    trigger_reason: str
    recommended_action: str


@router.get("/assignments", status_code=status.HTTP_200_OK)
def get_advisor_assignments() -> List[Dict[str, Any]]:
    return _assignments_db


@router.post("/interventions", status_code=status.HTTP_201_CREATED)
def trigger_academic_intervention(payload: InterventionCreate) -> Dict[str, Any]:
    intervention = {
        "id": str(uuid4()),
        "student_id": payload.student_id,
        "risk_level": payload.risk_level,
        "trigger_reason": payload.trigger_reason,
        "recommended_action": payload.recommended_action,
        "is_resolved": False
    }
    _interventions_db.append(intervention)
    return intervention
