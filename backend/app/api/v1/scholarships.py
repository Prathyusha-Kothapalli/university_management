from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.scholarship import Scholarship, ScholarshipApplication

router = APIRouter(prefix="/scholarships", tags=["Scholarships & Financial Aid"])

mock_scholarships = [
    Scholarship(
        id="sch-101",
        title="Merit Excellence Scholarship 2026",
        sponsor="UniSphere Foundation",
        amount_inr=75000.0,
        min_cgpa=3.75,
        eligible_departments=["Computer Science", "Electrical Eng", "Mechanical Eng"],
        deadline="2026-10-15",
        available_grants=25,
        status="Active",
    ),
    Scholarship(
        id="sch-102",
        title="Women in STEM Fellowship",
        sponsor="Tech Innovation Council",
        amount_inr=100000.0,
        min_cgpa=3.50,
        eligible_departments=["Computer Science", "Artificial Intelligence"],
        deadline="2026-11-01",
        available_grants=10,
        status="Active",
    ),
]

mock_applications = [
    ScholarshipApplication(
        id="app-501",
        scholarship_id="sch-101",
        student_id="UNI-2026-8890",
        student_name="Alex Morgan",
        cgpa=3.84,
        applied_at="2026-09-10",
        status="Under Review",
    )
]

@router.get("/", response_model=List[Scholarship])
def get_scholarships():
    """
    Retrieve list of active university scholarships and financial aid opportunities.
    """
    return mock_scholarships

@router.get("/applications", response_model=List[ScholarshipApplication])
def get_scholarship_applications():
    """
    Retrieve list of submitted student scholarship applications.
    """
    return mock_applications

@router.post("/apply/{scholarship_id}", response_model=ScholarshipApplication)
def apply_scholarship(scholarship_id: str):
    """
    Submit student application for a specific scholarship opportunity.
    """
    sch = next((s for s in mock_scholarships if s.id == scholarship_id), None)
    if not sch:
        raise HTTPException(status_code=404, detail="Scholarship not found")
    
    new_app = ScholarshipApplication(
        id=f"app-{len(mock_applications)+501}",
        scholarship_id=scholarship_id,
        student_id="UNI-2026-8890",
        student_name="Alex Morgan",
        cgpa=3.84,
        applied_at="2026-09-11",
        status="Submitted",
    )
    mock_applications.append(new_app)
    return new_app
