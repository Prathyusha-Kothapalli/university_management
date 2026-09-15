import uuid
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.scholarship_application import ScholarshipApplication
from app.services.scholarship_service import evaluate_scholarship_eligibility


class ApplyScholarshipSchema(BaseModel):
    student_id: uuid.UUID
    scholarship_name: str
    scholarship_type: str = "MERIT"
    amount_awarded: float = 5000.0
    justification: Optional[str] = None


class ReviewScholarshipSchema(BaseModel):
    status: str # APPROVED, REJECTED, DISBURSED


router = APIRouter(
    prefix="/scholarship-applications",
    tags=["Scholarship Management"]
)


@router.post("/")
def apply_for_scholarship(data: ApplyScholarshipSchema, db: Session = Depends(get_db)):
    app_obj = ScholarshipApplication(
        student_id=data.student_id,
        scholarship_name=data.scholarship_name,
        scholarship_type=data.scholarship_type,
        amount_awarded=data.amount_awarded,
        justification=data.justification,
        status="PENDING"
    )
    db.add(app_obj)
    db.commit()
    db.refresh(app_obj)
    return {"message": "Scholarship application submitted", "application": app_obj}


@router.get("/")
def list_scholarship_applications(student_id: Optional[uuid.UUID] = None, db: Session = Depends(get_db)):
    query = select(ScholarshipApplication)
    if student_id:
        query = query.where(ScholarshipApplication.student_id == student_id)

    results = db.execute(query).scalars().all()
    return {"applications": results, "count": len(results)}


@router.put("/{application_id}/review")
def review_scholarship_application(application_id: uuid.UUID, data: ReviewScholarshipSchema, db: Session = Depends(get_db)):
    app_obj = db.get(ScholarshipApplication, application_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Scholarship application not found")

    app_obj.status = data.status
    db.commit()
    db.refresh(app_obj)
    return {"message": f"Scholarship application {data.status}", "application": app_obj}


@router.get("/evaluate-eligibility")
def evaluate_eligibility(gpa: float = 3.8, family_income: float = 40000.0, merit_rank: int = 5):
    return evaluate_scholarship_eligibility(gpa, family_income, merit_rank)
