import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.finance_expansion import (
    InstallmentPlanCreate,
    InstallmentPlanResponse,
    GatewayConfigCreate,
    GatewayConfigResponse,
    PaymentWebhookPayload,
)
from app.services import finance_expansion_service

router = APIRouter(prefix="/finance-expansion", tags=["Finance & Gateway Expansion"])


@router.post("/installment-plans", response_model=InstallmentPlanResponse, status_code=status.HTTP_201_CREATED)
def create_installment_plan(
    data: InstallmentPlanCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Generate installment payment schedule for student fee."""
    return finance_expansion_service.create_installment_plan(
        db=db,
        data=data,
    )


@router.post("/gateway-configs", response_model=GatewayConfigResponse, status_code=status.HTTP_201_CREATED)
def configure_payment_gateway(
    data: GatewayConfigCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Register or update multi-tenant payment gateway API credentials."""
    return finance_expansion_service.register_gateway_config(
        db=db,
        data=data,
    )


@router.post("/webhooks/process-payment", status_code=status.HTTP_200_OK)
def process_gateway_webhook(
    payload: PaymentWebhookPayload,
    db: Session = Depends(get_db),
):
    """Process incoming payment gateway webhook notification."""
    txn = finance_expansion_service.process_payment_webhook(
        db=db,
        payload=payload,
    )
    return {"status": "SUCCESS", "transaction_id": str(txn.id)}
