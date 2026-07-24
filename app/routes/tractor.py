from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.dependencies import get_db
from app.services.tractor_service import TractorService
from app.schema.tractor_response import TractorProfileResponse

router = APIRouter()


@router.get(
    "/profile",
    response_model=TractorProfileResponse
)
def tractor_profile(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return TractorService.get_profile(
        db,
        user["customer_id"]
    )