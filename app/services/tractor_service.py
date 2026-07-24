from fastapi import HTTPException

from app.repositories.tractor_repository import TractorRepository


class TractorService:

    @staticmethod
    def get_profile(db, customer_id):

        tractor = TractorRepository.get_by_customer_id(
            db,
            customer_id
        )

        if tractor is None:
            raise HTTPException(
                status_code=404,
                detail="No tractor found"
            )

        return {
            "chassis_number": tractor.chassis_number,
            "model": tractor.model,
            "battery_serial": tractor.battery_serial,
            "motor_serial": tractor.motor_serial,
            "purchase_date": tractor.purchase_date,
            "warranty_expiry": tractor.warranty_expiry,
            "status": tractor.status
        }