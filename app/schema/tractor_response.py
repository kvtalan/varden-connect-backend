from datetime import date

from pydantic import BaseModel


class TractorProfileResponse(BaseModel):
    chassis_number: str
    model: str
    battery_serial: str
    motor_serial: str
    purchase_date: date
    warranty_expiry: date
    status: str