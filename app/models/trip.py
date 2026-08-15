from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)

    tractor_id = Column(
        Integer,
        ForeignKey("tractors.id"),
        nullable=False
    )

    start_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    end_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    start_soc = Column(Float)
    end_soc = Column(Float)

    distance = Column(Float, default=0)

    avg_speed = Column(Float, default=0)
    max_speed = Column(Float, default=0)

    energy_used = Column(Float, default=0)

    start_latitude = Column(Float)
    start_longitude = Column(Float)

    end_latitude = Column(Float)
    end_longitude = Column(Float)

    tractor = relationship(
        "Tractor",
        back_populates="trips"
    )