import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_payment_webhook_processing():
    payment_id = f"pay_{uuid.uuid4().hex[:8]}"
    student_id = str(uuid.uuid4())

    webhook_payload = {
        "provider": "stripe",
        "event_type": "payment_intent.succeeded",
        "payment_id": payment_id,
        "order_id": "ord_1001",
        "amount_in_cents": 125000,
        "currency": "USD",
        "student_id": student_id,
        "signature": "valid_signature_hash"
    }

    response = client.post("/api/v1/payment-gateways/webhook", json=webhook_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "SUCCESS"
    assert data["receipt"]["amount_paid"] == 1250.0

    # Test idempotency (duplicate webhook call)
    dup_res = client.post("/api/v1/payment-gateways/webhook", json=webhook_payload)
    assert dup_res.status_code == 200
    assert dup_res.json()["status"] == "DUPLICATE_IGNORED"
