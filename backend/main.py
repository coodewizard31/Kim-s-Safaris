from fastapi import FastAPI

from routes.payments import router as payments_router
from routes.bookings import router as bookings_router


app = FastAPI(
    title="Kim's Safaris API",
    description="Backend API for safari bookings and payments",
    version="1.0.0"
)


app.include_router(payments_router)
app.include_router(bookings_router)


@app.get("/")
async def home():
    return {
        "message": "Welcome to Kim's Safaris API"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "Kim's Safaris Backend"
    }