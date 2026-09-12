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
                email="test_transport_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Transport Manager",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_vehicle_fuel_and_maintenance_workflow(auth_headers: dict):
    client = TestClient(app)
    vehicle_id = str(uuid.uuid4())

    # 1. Log Fuel
    fuel_resp = client.post(
        "/api/v1/campus-transport/fuel-logs",
        headers=auth_headers,
        json={
            "vehicle_id": vehicle_id,
            "fuel_liters": 75.5,
            "cost_amount": 128.35,
            "odometer_reading": 34500.0,
        },
    )
    assert fuel_resp.status_code == 201
    assert fuel_resp.json()["fuel_liters"] == 75.5

    # 2. Schedule Maintenance
    maint_resp = client.post(
        "/api/v1/campus-transport/maintenance-logs",
        headers=auth_headers,
        json={
            "vehicle_id": vehicle_id,
            "service_type": "OIL_CHANGE",
            "description": "Routine 10,000 km oil filter replacement.",
            "cost_amount": 250.0,
            "scheduled_date": "2026-04-01T09:00:00Z",
        },
    )
    assert maint_resp.status_code == 201
    assert maint_resp.json()["status"] == "SCHEDULED"


def test_hostel_maintenance_ticket_creation(auth_headers: dict):
    client = TestClient(app)
    hostel_room_id = str(uuid.uuid4())
    student_id = str(uuid.uuid4())

    resp = client.post(
        "/api/v1/campus-transport/hostel-tickets",
        headers=auth_headers,
        json={
            "hostel_room_id": hostel_room_id,
            "student_id": student_id,
            "issue_category": "PLUMBING",
            "priority": "HIGH",
            "description": "Leaking faucet in private bathroom.",
        },
    )
    assert resp.status_code == 201
    assert resp.json()["status"] == "OPEN"
