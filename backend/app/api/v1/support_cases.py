import uuid
from typing import Optional, List
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.support_case import SupportCase
from app.models.case_note import CaseNote
from app.services.support_service import calculate_ticket_sla_deadline


class CreateSupportCaseSchema(BaseModel):
    student_id: uuid.UUID
    category: str = "ACADEMIC"
    priority: str = "MEDIUM"
    subject: str
    description: str


class AddCaseNoteSchema(BaseModel):
    author_name: str
    message: str
    is_internal_only: bool = False


class UpdateCaseStatusSchema(BaseModel):
    status: str
    assigned_agent: Optional[str] = None


router = APIRouter(
    prefix="/support-cases",
    tags=["Student Support & Help Desk"]
)


@router.post("/")
def create_support_case(data: CreateSupportCaseSchema, db: Session = Depends(get_db)):
    ticket_num = f"TICK-2026-{str(uuid.uuid4().hex[:6]).upper()}"
    case_obj = SupportCase(
        ticket_number=ticket_num,
        student_id=data.student_id,
        category=data.category,
        priority=data.priority,
        subject=data.subject,
        description=data.description,
        status="OPEN"
    )
    db.add(case_obj)
    db.commit()
    db.refresh(case_obj)

    sla = calculate_ticket_sla_deadline(data.priority)
    return {"message": "Support case created", "ticket_number": ticket_num, "case": case_obj, "sla": sla}


@router.get("/")
def list_support_cases(student_id: Optional[uuid.UUID] = None, category: Optional[str] = None, db: Session = Depends(get_db)):
    query = select(SupportCase)
    if student_id:
        query = query.where(SupportCase.student_id == student_id)
    if category:
        query = query.where(SupportCase.category == category)

    results = db.execute(query).scalars().all()
    return {"cases": results, "count": len(results)}


@router.get("/{case_id}")
def get_support_case_details(case_id: uuid.UUID, db: Session = Depends(get_db)):
    case_obj = db.get(SupportCase, case_id)
    if not case_obj:
        raise HTTPException(status_code=404, detail="Support case not found")

    notes = db.execute(select(CaseNote).where(CaseNote.case_id == case_id)).scalars().all()
    return {"case": case_obj, "notes": notes}


@router.post("/{case_id}/notes")
def add_case_note(case_id: uuid.UUID, data: AddCaseNoteSchema, db: Session = Depends(get_db)):
    case_obj = db.get(SupportCase, case_id)
    if not case_obj:
        raise HTTPException(status_code=404, detail="Support case not found")

    note = CaseNote(
        case_id=case_id,
        author_name=data.author_name,
        message=data.message,
        is_internal_only=data.is_internal_only
    )
    db.add(note)
    db.commit()
    return {"message": "Note added to case", "note": note}


@router.put("/{case_id}/status")
def update_case_status(case_id: uuid.UUID, data: UpdateCaseStatusSchema, db: Session = Depends(get_db)):
    case_obj = db.get(SupportCase, case_id)
    if not case_obj:
        raise HTTPException(status_code=404, detail="Support case not found")

    case_obj.status = data.status
    if data.assigned_agent:
        case_obj.assigned_agent = data.assigned_agent
    if data.status == "RESOLVED":
        case_obj.resolved_at = datetime.utcnow()

    db.commit()
    db.refresh(case_obj)
    return {"message": f"Case status updated to {data.status}", "case": case_obj}
