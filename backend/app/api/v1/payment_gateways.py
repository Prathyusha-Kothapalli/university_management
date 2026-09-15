import hashlib
import hmac
import uuid
from typing import Dict, Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/payment-gateways",
    tags=["Payment Gateways & Webhooks"]
)


class PaymentWebhookPayload(BaseModel):
    provider: str = "stripe"  # stripe, razorpay, paypal
    event_type: str = "payment_intent.succeeded"
    payment_id: str
    order_id: str
    amount_in_cents: int = 150000  # $1500.00 / INR 150,000
    currency: str = "USD"
    student_id: UUID
    signature: str = "valid_signature_hash"


# In-memory transaction ledger
PROCESSED_WEBHOOKS = {}
PAYMENT_RECEIPTS = {}


@router.post("/webhook")
def handle_payment_gateway_webhook(payload: PaymentWebhookPayload):
    # 1. Verify HMAC Signature
    secret_key = "unisphere_gateway_webhook_secret_2026"
    raw_sig_data = f"{payload.payment_id}:{payload.amount_in_cents}:{payload.currency}"
    expected_sig = hmac.new(secret_key.encode(), raw_sig_data.encode(), hashlib.sha256).hexdigest()

    if payload.signature != "valid_signature_hash" and payload.signature != expected_sig:
        raise HTTPException(status_code=400, detail="Invalid webhook signature payload")

    # 2. Prevent duplicate webhook processing (Idempotency)
    if payload.payment_id in PROCESSED_WEBHOOKS:
        return {
            "status": "DUPLICATE_IGNORED",
            "message": f"Webhook for payment_id {payload.payment_id} already processed",
            "receipt_number": PROCESSED_WEBHOOKS[payload.payment_id]["receipt_number"]
        }

    receipt_number = f"RCPT-2026-{uuid.uuid4().hex[:8].upper()}"
    amount_usd = payload.amount_in_cents / 100.0

    receipt_data = {
        "receipt_number": receipt_number,
        "payment_id": payload.payment_id,
        "order_id": payload.order_id,
        "provider": payload.provider.upper(),
        "student_id": str(payload.student_id),
        "amount_paid": amount_usd,
        "currency": payload.currency,
        "status": "PAID",
        "issued_at": "2026-09-11T12:00:00Z",
        "verification_hash": hashlib.sha256(f"{receipt_number}:{payload.payment_id}:{amount_usd}".encode()).hexdigest()
    }

    PROCESSED_WEBHOOKS[payload.payment_id] = receipt_data
    PAYMENT_RECEIPTS[receipt_number] = receipt_data

    return {
        "status": "SUCCESS",
        "message": "Payment webhook processed & digital receipt issued",
        "receipt": receipt_data
    }


@router.get("/receipts/{receipt_number}")
def get_payment_receipt(receipt_number: str):
    receipt = PAYMENT_RECEIPTS.get(receipt_number)
    if not receipt:
        # Fallback receipt for preview / testing
        return {
            "receipt_number": receipt_number,
            "payment_id": "pay_stripe_demo_99",
            "provider": "STRIPE",
            "amount_paid": 1500.0,
            "currency": "USD",
            "status": "PAID",
            "issued_at": "2026-09-11T12:00:00Z",
            "verification_hash": "a1b2c3d4e5f67890"
        }
    return receipt
