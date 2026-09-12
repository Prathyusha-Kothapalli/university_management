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
                email="test_finance_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Finance Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_fee_installment_plan_generation(auth_headers: dict):
    client = TestClient(app)
    student_fee_id = str(uuid.uuid4())

    resp = client.post(
        "/api/v1/finance-expansion/installment-plans",
        headers=auth_headers,
        json={
            "student_fee_id": student_fee_id,
            "total_installments": 4,
            "frequency_months": 1,
            "total_amount": 8000.0,
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["total_installments"] == 4
    assert len(data["installments"]) == 4
    assert data["installments"][0]["amount"] == 2000.0


def test_gateway_configuration_and_webhook(auth_headers: dict):
    client = TestClient(app)
    payment_id = str(uuid.uuid4())

    # 1. Register Config
    config_resp = client.post(
        "/api/v1/finance-expansion/gateway-configs",
        headers=auth_headers,
        json={
            "provider_name": "STRIPE",
            "api_key_masked": "sk_test_51...99xZ",
            "webhook_secret_masked": "whsec_88...11a",
            "environment_mode": "SANDBOX",
        },
    )
    assert config_resp.status_code == 201
    assert config_resp.json()["is_active"] is True

    # 2. Process Webhook
    webhook_resp = client.post(
        "/api/v1/finance-expansion/webhooks/process-payment",
        json={
            "payment_id": payment_id,
            "gateway_reference": "ch_3N9x...99",
            "provider_name": "STRIPE",
            "status": "SUCCESS",
            "raw_response": {"charge_id": "ch_123", "fee_captured": 8000.0},
        },
    )
    assert webhook_resp.status_code == 200
    assert webhook_resp.json()["status"] == "SUCCESS"
