from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertRepository:

    @staticmethod
    def create(db: Session, alert: Alert):
        db.add(alert)
        db.commit()
        db.refresh(alert)
        return alert

    @staticmethod
    def get_by_tractor_id(
        db: Session,
        tractor_id: int,
        limit: int = 100
    ):
        return (
            db.query(Alert)
            .filter(Alert.tractor_id == tractor_id)
            .order_by(Alert.created_at.desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def mark_as_read(
        db: Session,
        alert_id: int
    ):
        alert = (
            db.query(Alert)
            .filter(Alert.id == alert_id)
            .first()
        )

        if alert:
            alert.is_read = True
            db.commit()
            db.refresh(alert)

        return alert