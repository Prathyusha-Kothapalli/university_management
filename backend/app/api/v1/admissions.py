import uuid
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.admission_application import AdmissionApplication
from app.models.entrance_exam_result import EntranceExamResult
from app.services.admission_service import generate_program_merit_rankings


class ApplicationSubmitSchema(BaseModel):
    applicant_name: str
    email: EmailStr
    phone: Optional[str] = None
    program_id: uuid.UUID
    university_id: uuid.UUID
    gpa_score: float = 3.5


class ReviewApplicationSchema(BaseModel):
    status: str
    reviewer_notes: Optional[str] = None


class ExamResultSchema(BaseModel):
    application_id: uuid.UUID
    exam_code: str = "UNISPHERE_SAT_2026"
    total_score: float
    percentile: float


router = APIRouter(
    prefix="/admissions",
    tags=["Admissions & Enrollment"]
)


@router.post("/applications")
def submit_application(data: ApplicationSubmitSchema, db: Session = Depends(get_db)):
    app_obj = AdmissionApplication(
        applicant_name=data.applicant_name,
        email=data.email,
        phone=data.phone,
        program_id=data.program_id,
        university_id=data.university_id,
        gpa_score=data.gpa_score,
        status="SUBMITTED"
    )
    db.add(app_obj)
    db.commit()
    db.refresh(app_obj)
    return {"message": "Admission application submitted successfully", "application": app_obj}


@router.get("/applications")
def list_applications(program_id: Optional[uuid.UUID] = None, db: Session = Depends(get_db)):
    query = select(AdmissionApplication)
    if program_id:
        query = query.where(AdmissionApplication.program_id == program_id)

    results = db.execute(query).scalars().all()
    return {"applications": results, "count": len(results)}


@router.get("/applications/{app_id}")
def get_application_details(app_id: uuid.UUID, db: Session = Depends(get_db)):
    app_obj = db.get(AdmissionApplication, app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj


@router.put("/applications/{app_id}/review")
def review_application(app_id: uuid.UUID, data: ReviewApplicationSchema, db: Session = Depends(get_db)):
    app_obj = db.get(AdmissionApplication, app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")

    app_obj.status = data.status
    if data.reviewer_notes:
        app_obj.reviewer_notes = data.reviewer_notes

    db.commit()
    db.refresh(app_obj)
    return {"message": f"Application status updated to {data.status}", "application": app_obj}


@router.post("/exam-results")
def record_exam_result(data: ExamResultSchema, db: Session = Depends(get_db)):
    app_obj = db.get(AdmissionApplication, data.application_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")

    app_obj.entrance_exam_score = data.total_score
    app_obj.status = "EXAM_REGISTERED"

    exam_res = EntranceExamResult(
        application_id=data.application_id,
        exam_code=data.exam_code,
        total_score=data.total_score,
        percentile=data.percentile
    )
    db.add(exam_res)
    db.commit()
    return {"message": "Entrance exam score recorded successfully", "exam_result": exam_res}


@router.get("/merit-rankings/{program_id}")
def get_merit_rankings(program_id: uuid.UUID, db: Session = Depends(get_db)):
    rankings = generate_program_merit_rankings(db, program_id)
    return {"program_id": str(program_id), "rankings": rankings}
