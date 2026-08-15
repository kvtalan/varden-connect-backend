from sqlalchemy.orm import Session

from app.models.trip import Trip


class TripRepository:

    @staticmethod
    def create(db: Session, trip: Trip):
        db.add(trip)
        db.commit()
        db.refresh(trip)
        return trip

    @staticmethod
    def get_active_trip(
        db: Session,
        tractor_id: int
    ):
        return (
            db.query(Trip)
            .filter(
                Trip.tractor_id == tractor_id,
                Trip.end_time == None
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        trip: Trip
    ):
        db.commit()
        db.refresh(trip)
        return trip

    @staticmethod
    def get_history(
        db: Session,
        tractor_id: int,
        limit: int = 100
    ):
        return (
            db.query(Trip)
            .filter(
                Trip.tractor_id == tractor_id
            )
            .order_by(
                Trip.start_time.desc()
            )
            .limit(limit)
            .all()
        )