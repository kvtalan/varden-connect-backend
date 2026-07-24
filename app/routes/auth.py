from datetime import datetime, timedelta
import random

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.customer import Customer
from app.models.otp import OTP
from app.models.tractor import Tractor
from app.schema.chassis import ChassisRequest
from app.schema.verify_otp import VerifyOTPRequest
from app.security import create_access_token

router = APIRouter()


@router.post("/send-otp")
def send_otp(request: ChassisRequest, db: Session = Depends(get_db)):

    tractor = (
        db.query(Tractor)
        .filter(Tractor.chassis_number == request.chassis_number)
        .first()
    )

    if tractor is None:
        raise HTTPException(status_code=404, detail="Invalid chassis number")

    if tractor.status != "ACTIVE":
        raise HTTPException(
            status_code=403,
            detail="Tractor is not activated"
        )

    customer = (
        db.query(Customer)
        .filter(Customer.id == tractor.customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    otp = str(random.randint(100000, 999999))

    otp_record = OTP(
        customer_id=customer.id,
        otp=otp,
        expires_at=datetime.utcnow() + timedelta(minutes=5)
    )

    db.add(otp_record)
    db.commit()

    print(f"OTP for {customer.phone}: {otp}")

    masked_phone = (
        customer.phone[:2]
        + "******"
        + customer.phone[-2:]
    )

    return {
        "message": "OTP sent successfully",
        "phone": masked_phone
    }


@router.post("/verify-otp")
def verify_otp(request: VerifyOTPRequest, db: Session = Depends(get_db)):

    tractor = (
        db.query(Tractor)
        .filter(Tractor.chassis_number == request.chassis_number)
        .first()
    )

    if tractor is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid chassis number"
        )

    otp_record = (
        db.query(OTP)
        .filter(
            OTP.customer_id == tractor.customer_id,
            OTP.otp == request.otp,
            OTP.is_used == False
        )
        .order_by(OTP.created_at.desc())
        .first()
    )

    if otp_record is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    if otp_record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="OTP expired"
        )

    otp_record.is_used = True
    db.commit()

    token = create_access_token(
        {
            "customer_id": tractor.customer_id,
            "chassis": tractor.chassis_number
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }