import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_transport_vehicle_maintenance_and_fuel_logging():
    vehicle_id = str(uuid.uuid4())

    # 1. Log maintenance
    maint_payload = {
        "vehicle_id": vehicle_id,
        "service_type": "SCHEDULED_SERVICING",
        "odometer_km": 48000.0,
        "cost_usd": 420.0,
        "description": "Full engine tuning and tire rotation."
    }

    maint_res = client.post("/api/v1/transport-maintenance/log-maintenance", json=maint_payload)
    assert maint_res.status_code == 200
    assert maint_res.json()["record"]["cost_usd"] == 420.0

    # 2. Log fuel
    fuel_payload = {
        "vehicle_id": vehicle_id,
        "fuel_liters": 150.0,
        "price_per_liter": 1.40,
        "current_odometer_km": 48300.0
    }

    fuel_res = client.post("/api/v1/transport-maintenance/log-fuel", json=fuel_payload)
    assert fuel_res.status_code == 200
    assert fuel_res.json()["fuel_entry"]["total_cost_usd"] == 210.0

    # 3. Retrieve history
    hist_res = client.get(f"/api/v1/transport-maintenance/vehicle/{vehicle_id}")
    assert hist_res.status_code == 200
    assert hist_res.json()["total_maintenance_cost_usd"] >= 420.0
