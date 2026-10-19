from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.payment import Payment


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.get("/methods")
async def get_payment_methods():
    return {
        "payment_methods": [
            {
                "id": "mpesa",
                "name": "M-Pesa",
                "description": "Pay using M-Pesa",
                "enabled": False
            },
            {
                "id": "visa",
                "name": "Visa",
                "description": "Pay using your Visa card",
                "enabled": False
            }
        ]
    }


@router.get("/records")
async def get_payment_records(
    db: Session = Depends(get_db)
):
    payments = db.query(Payment).all()

    return {
        "total": len(payments),
        "payments": [
            {
                "id": payment.id,
                "booking_id": payment.booking_id,
                "provider": payment.provider,
                "payment_method": payment.payment_method,
                "amount": str(payment.amount),
                "currency": payment.currency,
                "status": payment.status,
                "transaction_reference": payment.transaction_reference,
                "created_at": payment.created_at
            }
            for payment in payments
        ]
    }