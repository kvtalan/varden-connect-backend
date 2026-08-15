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

    @staticmethod
    def get_by_chassis_number(db: Session, chassis_number: str):
        return (
            db.query(Tractor)
            .filter(Tractor.chassis_number == chassis_number)
            .first()
        )