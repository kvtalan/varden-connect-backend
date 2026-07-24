from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base


class Tractor(Base):
    __tablename__ = "tractors"

    id = Column(Integer, primary_key=True, index=True)

    chassis_number = Column(String, unique=True, nullable=False)

    model = Column(String, nullable=False)

    battery_serial = Column(String, unique=True)

    motor_serial = Column(String, unique=True)

    purchase_date = Column(Date)

    warranty_expiry = Column(Date)

    status = Column(String, default="active")

    customer_id = Column(Integer, ForeignKey("customers.id"))