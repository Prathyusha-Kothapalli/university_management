import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/curriculum",
    tags=["Outcome-Based Education"]
)


class CourseOutcome(BaseModel):
    co_code: str  # e.g., CO1, CO2
    statement: str
    target_attainment_pct: float = 75.0


class ProgramOutcome(BaseModel):
    po_code: str  # e.g., PO1, PO2
    title: str
    description: str


class COPOMappingRequest(BaseModel):
    course_code: str
    program_code: str
    mappings: Dict[str, Dict[str, int]]  # e.g., {"CO1": {"PO1": 3, "PO2": 2}}


# In-memory storage for OBE mappings & accreditation data
OBE_MAPPINGS = {}
ACCREDITATION_REPORTS = {}


@router.post("/co-po-mapping")
def map_co_po_matrix(req: COPOMappingRequest):
    mapping_key = f"{req.course_code}_{req.program_code}"
    
    # Calculate average correlation strength
    total_weights = 0
    total_cells = 0
    for co, po_map in req.mappings.items():
        for po, weight in po_map.items():
            total_weights += weight
            total_cells += 1
            
    avg_correlation = round(total_weights / max(total_cells, 1), 2)

    entry = {
        "mapping_id": str(uuid.uuid4()),
        "course_code": req.course_code,
        "program_code": req.program_code,
        "matrix": req.mappings,
        "average_correlation_score": avg_correlation,
        "updated_at": "2026-09-11T12:00:00Z"
    }

    OBE_MAPPINGS[mapping_key] = entry

    return {
        "message": "CO-PO mapping matrix updated successfully",
        "mapping": entry
    }


@router.get("/co-po-mapping/{course_code}")
def get_co_po_mapping(course_code: str, program_code: str = "BTECH_CS"):
    mapping_key = f"{course_code}_{program_code}"
    mapping = OBE_MAPPINGS.get(mapping_key, {
        "mapping_id": "map-default-001",
        "course_code": course_code,
        "program_code": program_code,
        "matrix": {
            "CO1": {"PO1": 3, "PO2": 2, "PO3": 1},
            "CO2": {"PO1": 2, "PO3": 3, "PO4": 2},
            "CO3": {"PO2": 3, "PO4": 3, "PO5": 2}
        },
        "average_correlation_score": 2.33,
        "updated_at": "2026-09-11T12:00:00Z"
    })

    return mapping


@router.get("/accreditation-report")
def generate_accreditation_report(framework: str = "NAAC", program_code: str = "BTECH_CS"):
    report_id = str(uuid.uuid4())
    
    return {
        "report_id": report_id,
        "accreditation_body": framework.upper(),
        "program_code": program_code,
        "criteria_compliance": {
            "Criterion_1_Curricular_Aspects": 92.5,
            "Criterion_2_Teaching_Learning": 88.0,
            "Criterion_3_Research_Innovation": 85.4,
            "Criterion_4_Infrastructure": 94.0,
            "Criterion_5_Student_Support": 91.2,
            "Criterion_6_Governance_Leadership": 89.5,
            "Criterion_7_Institutional_Values": 93.0
        },
        "cumulative_gpa_score": 3.65,
        "accreditation_grade": "A++" if framework.upper() == "NAAC" else "Tier-1 Accredited",
        "generated_at": "2026-09-11T12:00:00Z"
    }
