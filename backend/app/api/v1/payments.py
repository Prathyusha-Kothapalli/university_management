from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.payment import Payment
from app.schemas.payment import (
    PaymentCreate,
    PaymentUpdate,
    PaymentResponse,
)


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post(
    "/",
    response_model=PaymentResponse
)
def create_payment(
    payment_data: PaymentCreate,
    db: Session = Depends(get_db)
):
    try:
        payment = Payment(
            **payment_data.model_dump()
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[PaymentResponse]
)
def get_payments(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Payment)
    )

    return result.scalars().all()


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment(
    payment_id: UUID,
    db: Session = Depends(get_db)
):
    payment = db.get(
        Payment,
        payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.put(
    "/{payment_id}",
    response_model=PaymentResponse
)
def update_payment(
    payment_id: UUID,
    payment_data: PaymentUpdate,
    db: Session = Depends(get_db)
):
    payment = db.get(
        Payment,
        payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    try:
        update_data = payment_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(payment, key):
                setattr(
                    payment,
                    key,
                    value
                )

        db.commit()
        db.refresh(payment)

        return payment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{payment_id}")
def delete_payment(
    payment_id: UUID,
    db: Session = Depends(get_db)
):
    payment = db.get(
        Payment,
        payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    db.delete(payment)
    db.commit()

    return {
        "message": "Payment deleted successfully"
    }
