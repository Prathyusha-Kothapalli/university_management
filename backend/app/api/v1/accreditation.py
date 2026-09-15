import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

router = APIRouter(
    prefix="/accreditation",
    tags=["Accreditation & Self-Study Dossier"]
)


class AccreditationSubmissionRequest(BaseModel):
    department_id: UUID
    framework: str = "NAAC"  # NAAC, ABET, NBA
    self_study_score: float = 3.78  # Cumulative score out of 4.0
    evaluation_year: int = 2026


# In-memory storage for accreditation dossiers
ACCREDITATION_DOSSIERS = {}


@router.post("/submit-dossier")
def submit_accreditation_dossier(req: AccreditationSubmissionRequest):
    dossier_id = str(uuid.uuid4())
    dept_str = str(req.department_id)

    dossier_entry = {
        "dossier_id": dossier_id,
        "department_id": dept_str,
        "framework": req.framework.upper(),
        "self_study_score": req.self_study_score,
        "status": "SUBMITTED_FOR_AUDIT",
        "submitted_at": "2026-09-11T12:30:00Z",
        "audit_criteria": {
            "Criterion_1_Curricular_Design": 95.0,
            "Criterion_2_Teaching_Evaluation": 91.5,
            "Criterion_3_Research_Output": 88.0,
            "Criterion_4_Infrastructure_Labs": 96.0,
            "Criterion_5_Student_Progression": 93.5
        }
    }

    ACCREDITATION_DOSSIERS[dossier_id] = dossier_entry

    return {
        "message": f"Accreditation dossier submitted for {req.framework.upper()} audit",
        "dossier": dossier_entry
    }


@router.get("/dossier/{dossier_id}")
def get_accreditation_dossier(dossier_id: UUID):
    d_str = str(dossier_id)
    dossier = ACCREDITATION_DOSSIERS.get(d_str, {
        "dossier_id": d_str,
        "department_id": "dept-cs-01",
        "framework": "NAAC",
        "self_study_score": 3.82,
        "status": "ACCREDITED_A_PLUS_PLUS",
        "audit_criteria": {
            "Criterion_1_Curricular_Design": 96.5,
            "Criterion_2_Teaching_Evaluation": 92.0,
            "Criterion_3_Research_Output": 89.5,
            "Criterion_4_Infrastructure_Labs": 97.0,
            "Criterion_5_Student_Progression": 94.0
        }
    })

    return dossier
