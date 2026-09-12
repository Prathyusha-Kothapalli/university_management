import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_prerequisite_check_endpoint():
    course_id = str(uuid.uuid4())
    response = client.get(f"/api/v1/courses/{course_id}/prerequisites-check?completed_codes=CS201&completed_codes=MATH202")
    assert response.status_code == 200
    data = response.json()
    assert data["is_eligible"] is True
    assert len(data["missing_prerequisites"]) == 0


def test_course_enrollment_prerequisite_failure():
    offering_id = str(uuid.uuid4())
    student_id = str(uuid.uuid4())

    payload = {
        "student_id": student_id,
        "offering_id": offering_id,
        "completed_prerequisite_codes": [],
        "current_schedule_slots": []
    }

    response = client.post(f"/api/v1/courses/{offering_id}/enroll", json=payload)
    assert response.status_code == 400
    assert "Prerequisite failure" in response.json()["detail"]


def test_course_enrollment_success():
    offering_id = str(uuid.uuid4())
    student_id = str(uuid.uuid4())

    payload = {
        "student_id": student_id,
        "offering_id": offering_id,
        "completed_prerequisite_codes": ["CS201", "MATH202"],
        "current_schedule_slots": ["MON_0900"]
    }

    response = client.post(f"/api/v1/courses/{offering_id}/enroll", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ENROLLED"
    assert data["student_id"] == student_id
