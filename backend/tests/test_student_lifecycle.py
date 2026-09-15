import pytest
import uuid
from fastapi.testclient import TestClient

from app.main import app
from app.models.user import User
from app.core.security import create_access_token
from app.database.session import SessionLocal


@pytest.fixture
def auth_headers():
    db = SessionLocal()
    try:
        user = db.query(User).first()
        if not user:
            user = User(
                id=uuid.uuid4(),
                email="test_lifecycle_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Lifecycle Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_academic_hold_lifecycle(auth_headers: dict):
    client = TestClient(app)
    student_id = str(uuid.uuid4())

    # 1. Place Hold
    hold_resp = client.post(
        "/api/v1/student-lifecycle/holds",
        headers=auth_headers,
        json={
            "student_id": student_id,
            "hold_type": "FINANCIAL",
            "reason": "Unpaid library fees ($150)",
        },
    )
    assert hold_resp.status_code == 201
    hold_data = hold_resp.json()
    assert hold_data["is_active"] is True
    hold_id = hold_data["id"]

    # 2. List Holds
    list_resp = client.get(
        f"/api/v1/student-lifecycle/holds/student/{student_id}",
        headers=auth_headers,
    )
    assert list_resp.status_code == 200
    assert len(list_resp.json()) == 1

    # 3. Resolve Hold
    resolve_resp = client.put(
        f"/api/v1/student-lifecycle/holds/{hold_id}/resolve",
        headers=auth_headers,
    )
    assert resolve_resp.status_code == 200
    assert resolve_resp.json()["is_active"] is False


def test_conduct_case_creation(auth_headers: dict):
    client = TestClient(app)
    student_id = str(uuid.uuid4())

    resp = client.post(
        "/api/v1/student-lifecycle/conduct-cases",
        headers=auth_headers,
        json={
            "student_id": student_id,
            "incident_title": "Unauthorized Absence during Exam",
            "incident_description": "Student missed mid-term exam without medical certificate.",
            "severity": "MINOR",
            "action_taken": "Written warning issued.",
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["status"] == "UNDER_INVESTIGATION"
    assert data["severity"] == "MINOR"
