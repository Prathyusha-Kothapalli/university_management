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
                email="test_obe_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="OBE Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_obe_co_po_attainment_flow(auth_headers: dict):
    client = TestClient(app)
    offering_id = str(uuid.uuid4())
    program_id = str(uuid.uuid4())

    # 1. Add CO
    co_resp = client.post(
        f"/api/v1/curriculum-obe/course-outcomes/{offering_id}",
        headers=auth_headers,
        json={
            "code": "CO101",
            "description": "Understand core data structures and complexity bounds",
            "bloom_taxonomy_level": "ANALYZE",
            "target_attainment_pct": 80.0,
        },
    )
    assert co_resp.status_code == 201
    co_id = co_resp.json()["id"]

    # 2. Add PO
    po_resp = client.post(
        f"/api/v1/curriculum-obe/program-outcomes/{program_id}",
        headers=auth_headers,
        json={
            "code": "PO-CS-01",
            "title": "Engineering Knowledge",
            "description": "Apply mathematics and computing fundamentals.",
        },
    )
    assert po_resp.status_code == 201
    po_id = po_resp.json()["id"]

    # 3. Map CO to PO
    map_resp = client.post(
        "/api/v1/curriculum-obe/mappings",
        headers=auth_headers,
        json={
            "course_outcome_id": co_id,
            "program_outcome_id": po_id,
            "weight": 3,
        },
    )
    assert map_resp.status_code == 201
    assert map_resp.json()["weight"] == 3

    # 4. Get Attainment Matrix
    matrix_resp = client.get(
        f"/api/v1/curriculum-obe/attainment-matrix/{offering_id}",
        headers=auth_headers,
    )
    assert matrix_resp.status_code == 200
    matrix_data = matrix_resp.json()
    assert len(matrix_data) == 1
    assert matrix_data[0]["co_code"] == "CO101"
    assert matrix_data[0]["mapped_pos"][0]["po_code"] == "PO-CS-01"
    assert matrix_data[0]["mapped_pos"][0]["weight"] == 3
