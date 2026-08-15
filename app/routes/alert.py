from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.dependencies import get_db
from app.repositories.tractor_repository import TractorRepository
from app.repositories.alert_repository import AlertRepository

router = APIRouter(
    prefix="/tractor",
    tags=["Alerts"]
)


@router.get("/alerts")
def get_alerts(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    tractor = TractorRepository.get_by_customer_id(
        db,
        user["customer_id"]
    )

    if tractor is None:
        return []

    return AlertRepository.get_by_tractor_id(
        db,
        tractor.id
    )