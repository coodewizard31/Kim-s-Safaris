from sqlalchemy import Column, Integer, String, Numeric
from database import Base


class SafariPackage(Base):
    __tablename__ = "safari_packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(String(1000))
    price = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(3), nullable=False, default="KES")