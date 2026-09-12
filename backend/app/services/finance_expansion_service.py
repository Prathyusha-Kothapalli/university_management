import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.finance_expansion import (
    FeeInstallmentPlan,
    FeeInstallment,
    PaymentGatewayConfig,
    PaymentTransaction,
)
from app.schemas.finance_expansion import (
    InstallmentPlanCreate,
    GatewayConfigCreate,
    PaymentWebhookPayload,
)


def create_installment_plan(
    db: Session,
    data: InstallmentPlanCreate
) -> FeeInstallmentPlan:
    plan = FeeInstallmentPlan(
        student_fee_id=data.student_fee_id,
        total_installments=data.total_installments,
        frequency_months=data.frequency_months,
        total_amount=data.total_amount,
        is_approved=True,
    )
    db.add(plan)
    db.flush()

    installment_amt = data.total_amount / max(data.total_installments, 1)
    now = datetime.utcnow()

    for i in range(1, data.total_installments + 1):
        due = now + timedelta(days=30 * (i - 1) * data.frequency_months)
        inst = FeeInstallment(
            installment_plan_id=plan.id,
            installment_number=i,
            amount=installment_amt,
            due_date=due,
            status="PENDING",
        )
        db.add(inst)

    db.commit()
    db.refresh(plan)
    return plan


def register_gateway_config(
    db: Session,
    data: GatewayConfigCreate
) -> PaymentGatewayConfig:
    config = PaymentGatewayConfig(
        provider_name=data.provider_name.upper(),
        api_key_masked=data.api_key_masked,
        webhook_secret_masked=data.webhook_secret_masked,
        is_active=True,
        environment_mode=data.environment_mode,
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    return config


def process_payment_webhook(
    db: Session,
    payload: PaymentWebhookPayload
) -> PaymentTransaction:
    txn = PaymentTransaction(
        payment_id=payload.payment_id,
        gateway_reference=payload.gateway_reference,
        provider_name=payload.provider_name,
        status=payload.status,
        raw_response=payload.raw_response,
    )
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn
