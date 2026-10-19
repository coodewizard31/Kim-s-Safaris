from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from database import get_db
from models.booking import Booking
from models.safari import SafariPackage


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


class BookingCreate(BaseModel):
    customer_name: str = Field(min_length=2)
    email: EmailStr
    phone: str = Field(min_length=7)
    safari_package_id: int = Field(gt=0)
    travel_date: date
    number_of_guests: int = Field(gt=0)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    # Check whether the safari package exists
    safari = db.get(
        SafariPackage,
        booking.safari_package_id
    )

    if not safari:
        raise HTTPException(
            status_code=404,
            detail="Safari package not found"
        )

    # Validate the travel date
    if booking.travel_date < date.today():
        raise HTTPException(
            status_code=400,
            detail="Travel date cannot be in the past"
        )

    # Create a pending booking
    new_booking = Booking(
        customer_name=booking.customer_name,
        email=str(booking.email),
        phone=booking.phone,
        safari_package_id=booking.safari_package_id,
        travel_date=booking.travel_date,
        number_of_guests=booking.number_of_guests,
        status="pending"
    )

    # Save booking to PostgreSQL
    db.add(new_booking)

    try:
        db.commit()
        db.refresh(new_booking)

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to save booking"
        )

    return {
        "message": "Booking created successfully",
        "booking_id": new_booking.id,
        "customer_name": new_booking.customer_name,
        "safari_package": safari.name,
        "travel_date": new_booking.travel_date,
        "number_of_guests": new_booking.number_of_guests,
        "status": new_booking.status
    }