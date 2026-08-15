from sqlalchemy.orm import Session

from app.models.telemetry import Telemetry


class TelemetryRepository:

    @staticmethod
    def create(db: Session, telemetry: Telemetry):
        db.add(telemetry)
        db.commit()
        db.refresh(telemetry)
        return telemetry

    @staticmethod
    def get_latest_by_tractor_id(db: Session, tractor_id: int):
        return (
            db.query(Telemetry)
            .filter(Telemetry.tractor_id == tractor_id)
            .order_by(Telemetry.timestamp.desc())
            .first()
        )

    @staticmethod
    def get_history_by_tractor_id(
    db,
    tractor_id: int,
    limit: int = 100
):
        return (
        db.query(Telemetry)
        .filter(
            Telemetry.tractor_id == tractor_id
        )
        .order_by(
            Telemetry.timestamp.desc()
        )
        .limit(limit)
        .all()
    )