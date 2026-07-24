from pydantic import BaseModel


class VerifyOTPRequest(BaseModel):
    chassis_number: str
    otp: str