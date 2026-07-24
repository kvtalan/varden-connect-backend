from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    phone = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=True)

    address = Column(String)

    village = Column(String)

    district = Column(String)

    state = Column(String)

    is_phone_verified = Column(Boolean, default=False)