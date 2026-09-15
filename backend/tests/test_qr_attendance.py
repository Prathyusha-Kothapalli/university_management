import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)
client = TestClient(app)

def test_qr_attendance_token_generation_and_scanning():
    session_id = str(uuid.uuid4())
    student_id = str(uuid.uuid4())

    gen_resp = client.get(f"/api/v1/attendance-records/qr/generate/{session_id}")
    assert gen_resp.status_code == 200
    qr_payload = gen_resp.json()["qr_token"]
    assert qr_payload.startswith("QR:")

    scan_resp = client.post("/api/v1/attendance-records/qr/scan", json={
        "qr_payload": qr_payload,
        "student_id": student_id
    })
    assert scan_resp.status_code == 200
    assert scan_resp.json()["success"] is True

def test_attendance_exemption_request():
    student_id = str(uuid.uuid4())
    course_id = str(uuid.uuid4())

    ex_resp = client.post("/api/v1/attendance-records/exemptions", json={
        "student_id": student_id,
        "course_id": course_id,
        "exemption_type": "MEDICAL",
        "start_date": "2026-09-15T00:00:00Z",
        "end_date": "2026-09-18T00:00:00Z",
        "reason": "Hospitalization for acute viral fever"
    })
    assert ex_resp.status_code == 200
    assert "exemption_id" in ex_resp.json()
