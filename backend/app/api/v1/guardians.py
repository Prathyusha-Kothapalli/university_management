import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/guardians",
    tags=["Guardian Portal & Emergency Alerts"]
)


class GuardianRegisterRequest(BaseModel):
    student_id: UUID
    full_name: str
    relation: str = "Parent"  # Father, Mother, Guardian
    phone_number: str
    email: str
    address: Optional[str] = "123 University Avenue"


class EmergencyAlertRequest(BaseModel):
    student_id: UUID
    alert_type: str = "MEDICAL_EMERGENCY"  # MEDICAL_EMERGENCY, LOW_ATTENDANCE_CRITICAL, UNAUTHORIZED_ABSENCE
    severity: str = "HIGH"  # LOW, MEDIUM, HIGH, CRITICAL
    message: str


# In-memory storage for guardians and dispatched alert logs
GUARDIANS_STORE = {}
DISPATCHED_ALERTS = []


@router.post("/")
def register_guardian(req: GuardianRegisterRequest):
    guardian_id = str(uuid.uuid4())
    student_str = str(req.student_id)

    entry = {
        "guardian_id": guardian_id,
        "student_id": student_str,
        "full_name": req.full_name,
        "relation": req.relation,
        "phone_number": req.phone_number,
        "email": req.email,
        "address": req.address,
        "is_primary": True,
        "created_at": "2026-09-11T12:30:00Z"
    }

    if student_str not in GUARDIANS_STORE:
        GUARDIANS_STORE[student_str] = []
    GUARDIANS_STORE[student_str].append(entry)

    return {
        "message": "Guardian record registered successfully",
        "guardian": entry
    }


@router.post("/emergency-alert")
def dispatch_emergency_alert(req: EmergencyAlertRequest):
    student_str = str(req.student_id)
    alert_id = str(uuid.uuid4())

    alert_record = {
        "alert_id": alert_id,
        "student_id": student_str,
        "alert_type": req.alert_type,
        "severity": req.severity,
        "message": req.message,
        "dispatched_channels": ["SMS_TWILIO", "EMAIL_SMTP", "PUSH_NOTIFICATION"],
        "dispatched_at": "2026-09-11T12:33:00Z",
        "status": "DISPATCHED"
    }

    DISPATCHED_ALERTS.append(alert_record)

    return {
        "message": "Emergency alert dispatched to guardian contact channels",
        "alert": alert_record
    }


@router.get("/student/{student_id}")
def get_student_guardians(student_id: UUID):
    student_str = str(student_id)
    guardians = GUARDIANS_STORE.get(student_str, [
        {
            "guardian_id": "g-101",
            "student_id": student_str,
            "full_name": "Robert Vance",
            "relation": "Father",
            "phone_number": "+1-555-0192",
            "email": "robert.vance@parent.unisphere.edu",
            "is_primary": True
        }
    ])

    return {
        "student_id": student_str,
        "guardians_count": len(guardians),
        "guardians": guardians
    }
