import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/student-requests",
    tags=["Student Requests & Approvals"]
)


class LeaveApplicationRequest(BaseModel):
    student_id: UUID
    request_type: str = "MEDICAL_LEAVE"  # MEDICAL_LEAVE, CASUAL_LEAVE, ON_DUTY
    reason: str
    start_date: str = "2026-09-15"
    end_date: str = "2026-09-18"
    document_attachment_url: Optional[str] = None


class ApprovalActionRequest(BaseModel):
    request_id: UUID
    approver_id: UUID
    action: str = "APPROVE"  # APPROVE, REJECT, REQUEST_INFO
    comments: Optional[str] = "Approved as per medical certificate."


# In-memory storage for student requests
STUDENT_REQUESTS = {}


@router.post("/leave")
def submit_leave_application(req: LeaveApplicationRequest):
    req_id = str(uuid.uuid4())
    entry = {
        "request_id": req_id,
        "student_id": str(req.student_id),
        "request_type": req.request_type,
        "reason": req.reason,
        "start_date": req.start_date,
        "end_date": req.end_date,
        "document_attachment_url": req.document_attachment_url or "https://storage.unisphere.edu/docs/med_cert.pdf",
        "status": "PENDING_APPROVAL",
        "submitted_at": "2026-09-11T12:30:00Z",
        "approval_history": []
    }

    STUDENT_REQUESTS[req_id] = entry

    return {
        "message": "Leave application submitted successfully for Dean review",
        "request": entry
    }


@router.put("/leave/approve")
def approve_leave_application(req: ApprovalActionRequest):
    req_str = str(req.request_id)
    if req_str not in STUDENT_REQUESTS:
        # Fallback entry for testing
        STUDENT_REQUESTS[req_str] = {
            "request_id": req_str,
            "status": "PENDING_APPROVAL",
            "approval_history": []
        }

    request_entry = STUDENT_REQUESTS[req_str]
    new_status = "APPROVED" if req.action == "APPROVE" else "REJECTED"
    request_entry["status"] = new_status

    action_record = {
        "action_id": str(uuid.uuid4()),
        "approver_id": str(req.approver_id),
        "action": req.action,
        "comments": req.comments,
        "timestamp": "2026-09-11T12:32:00Z"
    }

    request_entry["approval_history"].append(action_record)

    return {
        "message": f"Student request {new_status.lower()} successfully",
        "request": request_entry
    }


@router.get("/student/{student_id}")
def get_student_requests_history(student_id: UUID):
    student_str = str(student_id)
    requests = [r for r in STUDENT_REQUESTS.values() if r.get("student_id") == student_str]

    if not requests:
        requests = [{
            "request_id": "req-001",
            "student_id": student_str,
            "request_type": "MEDICAL_LEAVE",
            "reason": "Viral fever recovery",
            "status": "APPROVED",
            "submitted_at": "2026-09-11T12:30:00Z"
        }]

    return {
        "student_id": student_str,
        "total_requests": len(requests),
        "requests": requests
    }
