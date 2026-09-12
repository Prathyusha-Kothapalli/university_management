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
                email="test_iot_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Smart Campus Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_iot_device_and_building_control_workflow(auth_headers: dict):
    client = TestClient(app)
    classroom_id = str(uuid.uuid4())

    # 1. Register Device
    device_resp = client.post(
        "/api/v1/campus-iot/devices",
        headers=auth_headers,
        json={
            "device_name": "HVAC Controller A-101",
            "device_type": "HVAC_CONTROLLER",
            "classroom_id": classroom_id,
            "mac_address": "00:1B:44:11:3A:B7",
        },
    )
    assert device_resp.status_code == 201
    device_id = device_resp.json()["id"]

    # 2. Log Telemetry
    telem_resp = client.post(
        "/api/v1/campus-iot/telemetry",
        headers=auth_headers,
        json={
            "device_id": device_id,
            "metric_name": "TEMPERATURE_C",
            "metric_value": 21.8,
        },
    )
    assert telem_resp.status_code == 201
    assert telem_resp.json()["metric_value"] == 21.8

    # 3. Set Control
    ctrl_resp = client.post(
        "/api/v1/campus-iot/controls",
        headers=auth_headers,
        json={
            "classroom_id": classroom_id,
            "target_temperature_c": 22.5,
            "lighting_level_pct": 90,
            "is_occupied": True,
        },
    )
    assert ctrl_resp.status_code == 201
    assert ctrl_resp.json()["target_temperature_c"] == 22.5
