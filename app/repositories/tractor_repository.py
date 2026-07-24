from sqlalchemy.orm import Session

from app.models.tractor import Tractor


class TractorRepository:

    @staticmethod
    def get_by_customer_id(db: Session, customer_id: int):
        return (
            db.query(Tractor)
            .filter(Tractor.customer_id == customer_id)
            .first()
        )