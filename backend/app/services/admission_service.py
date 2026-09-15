import uuid
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.admission_application import AdmissionApplication
from app.models.entrance_exam_result import EntranceExamResult

def calculate_applicant_composite_score(gpa: float, exam_score: float) -> float:
    """Calculates weighted composite score (60% entrance exam + 40% GPA)."""
    gpa_percentage = (gpa / 4.0) * 100.0
    composite = (exam_score * 0.6) + (gpa_percentage * 0.4)
    return round(composite, 2)

def generate_program_merit_rankings(db: Session, program_id: uuid.UUID) -> List[Dict[str, Any]]:
    """Calculates program applicant rankings based on composite scores."""
    apps = db.execute(
        select(AdmissionApplication).where(AdmissionApplication.program_id == program_id)
    ).scalars().all()

    ranked_list = []
    for app in apps:
        exam_score = app.entrance_exam_score if app.entrance_exam_score else 75.0
        composite = calculate_applicant_composite_score(app.gpa_score, exam_score)
        ranked_list.append({
            "application_id": str(app.id),
            "applicant_name": app.applicant_name,
            "email": app.email,
            "gpa": app.gpa_score,
            "exam_score": exam_score,
            "composite_score": composite,
            "status": app.status
        })

    # Sort descending by composite score
    ranked_list.sort(key=lambda x: x["composite_score"], reverse=True)
    for rank, item in enumerate(ranked_list, start=1):
        item["rank"] = rank

    return ranked_list
