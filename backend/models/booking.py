from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.sql import func

from database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(200), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(30), nullable=False)

    safari_package_id = Column(
        Integer,
        ForeignKey("safari_packages.id"),
        nullable=False
    )

    travel_date = Column(Date, nullable=False)
    number_of_guests = Column(Integer, nullable=False)

    status = Column(String(30), nullable=False, default="pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )