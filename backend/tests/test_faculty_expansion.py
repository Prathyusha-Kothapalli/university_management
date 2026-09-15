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
                email="test_faculty_exp@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Faculty Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_faculty_qualification_and_appraisal(auth_headers: dict):
    client = TestClient(app)
    faculty_id = str(uuid.uuid4())
    academic_year_id = str(uuid.uuid4())

    # 1. Add Qualification
    qual_resp = client.post(
        f"/api/v1/faculty-expansion/qualifications?faculty_id={faculty_id}",
        headers=auth_headers,
        json={
            "degree_name": "Ph.D. Computer Science",
            "institution": "Stanford University",
            "field_of_study": "Machine Learning",
            "year_awarded": 2021,
        },
    )
    assert qual_resp.status_code == 201
    assert qual_resp.json()["is_verified"] is True

    # 2. Submit Appraisal
    appraisal_resp = client.post(
        f"/api/v1/faculty-expansion/appraisals?faculty_id={faculty_id}",
        headers=auth_headers,
        json={
            "academic_year_id": academic_year_id,
            "teaching_score": 4.8,
            "research_score": 4.5,
            "service_score": 4.0,
            "self_assessment": "Exceeded research output targets.",
            "reviewer_comments": "Outstanding performance in grant acquisition.",
        },
    )
    assert appraisal_resp.status_code == 201
    # 4.8*0.4 + 4.5*0.4 + 4.0*0.2 = 1.92 + 1.8 + 0.8 = 4.52
    assert round(appraisal_resp.json()["overall_rating"], 2) == 4.52

    # 3. Get Metrics
    metrics_resp = client.get(
        f"/api/v1/faculty-expansion/metrics/{faculty_id}",
        headers=auth_headers,
    )
    assert metrics_resp.status_code == 200
    assert metrics_resp.json()["qualification_count"] == 1.0
