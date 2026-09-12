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
                email="test_alumni_admin@university.edu",
                password_hash="hashed_pass_xyz",
                full_name="Alumni Director",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_alumni_profile_and_donation_flow(auth_headers: dict):
    client = TestClient(app)
    student_id = str(uuid.uuid4())

    # 1. Register Alumni Profile
    profile_resp = client.post(
        "/api/v1/alumni-endowment/profiles",
        headers=auth_headers,
        json={
            "student_id": student_id,
            "graduation_year": 2021,
            "current_company": "Google",
            "current_designation": "Staff Engineer",
            "linkedin_url": "https://linkedin.com/in/test-alumni",
            "is_mentor_available": True,
        },
    )
    assert profile_resp.status_code == 201
    profile_id = profile_resp.json()["id"]

    # 2. Create Fund
    fund_resp = client.post(
        "/api/v1/alumni-endowment/funds",
        headers=auth_headers,
        json={
            "fund_name": "Quantum Computing Chair Fund",
            "target_amount_usd": 250000.0,
            "category": "RESEARCH_CHAIR",
        },
    )
    assert fund_resp.status_code == 201
    fund_id = fund_resp.json()["id"]

    # 3. Donate
    donation_resp = client.post(
        "/api/v1/alumni-endowment/donations",
        headers=auth_headers,
        json={
            "alumni_profile_id": profile_id,
            "fund_id": fund_id,
            "amount_usd": 50000.0,
            "payment_reference": "DON-2026-9912",
        },
    )
    assert donation_resp.status_code == 201
    assert donation_resp.json()["amount_usd"] == 50000.0
