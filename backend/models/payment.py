from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    DateTime,
    UniqueConstraint
)
from sqlalchemy.sql import func

from database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False
    )

    provider = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(3), nullable=False)

    status = Column(String(30), nullable=False, default="pending")

    transaction_reference = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    __table_args__ = (
        UniqueConstraint(
            "provider",
            "transaction_reference",
            name="uq_provider_transaction_reference"
        ),
    )