from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)

    tractor_id = Column(
        Integer,
        ForeignKey("tractors.id"),
        nullable=False,
        index=True
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    soc = Column(Float)
    voltage = Column(Float)
    current = Column(Float)

    battery_temp = Column(Float)
    battery_health = Column(Float)

    motor_rpm = Column(Integer)
    motor_temp = Column(Float)
    torque = Column(Float)

    speed = Column(Float)

    gear = Column(String)
    mode = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    tractor = relationship("Tractor", back_populates="telemetry")