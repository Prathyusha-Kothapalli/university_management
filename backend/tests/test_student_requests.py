import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_leave_application_and_approval():
    student_id = str(uuid.uuid4())
    approver_id = str(uuid.uuid4())

    # 1. Submit leave request
    leave_payload = {
        "student_id": student_id,
        "request_type": "MEDICAL_LEAVE",
        "reason": "Dental surgery recovery",
        "start_date": "2026-09-20",
        "end_date": "2026-09-22"
    }

    sub_res = client.post("/api/v1/student-requests/leave", json=leave_payload)
    assert sub_res.status_code == 200
    req_id = sub_res.json()["request"]["request_id"]

    # 2. Approve leave request
    app_payload = {
        "request_id": req_id,
        "approver_id": approver_id,
        "action": "APPROVE",
        "comments": "Approved medical leave."
    }

    app_res = client.put("/api/v1/student-requests/leave/approve", json=app_payload)
    assert app_res.status_code == 200
    assert app_res.json()["request"]["status"] == "APPROVED"


def test_guardian_emergency_alert():
    student_id = str(uuid.uuid4())

    alert_payload = {
        "student_id": student_id,
        "alert_type": "MEDICAL_EMERGENCY",
        "severity": "HIGH",
        "message": "Student admitted to campus infirmary for observation."
    }

    response = client.post("/api/v1/guardians/emergency-alert", json=alert_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["alert"]["status"] == "DISPATCHED"
    assert "SMS_TWILIO" in data["alert"]["dispatched_channels"]
