from pydantic import BaseModel


class ChassisRequest(BaseModel):
    chassis_number: str