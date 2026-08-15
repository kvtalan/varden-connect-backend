from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.services.telemetry_service import TelemetryService
from app.schema.telemetry_response import TelemetryResponse
from app.schema.telemetry_create import TelemetryCreate
from typing import List
from fastapi import Query

router = APIRouter(
    prefix="/tractor",
    tags=["Telemetry"]
)


@router.get(
    "/live",
    response_model=TelemetryResponse
)
def get_live_data(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    telemetry = TelemetryService.get_live_data(
        db=db,
        customer_id=user.id
    )

    if telemetry is None:
        raise HTTPException(
            status_code=404,
            detail="Telemetry not found"
        )



    return telemetry
@router.post("/ingest")
def ingest_telemetry(
    telemetry: TelemetryCreate,
    db: Session = Depends(get_db)
):
    result = TelemetryService.create(db, telemetry)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Tractor not found"
        )

    return result

@router.get(
    "/history",
    response_model=List[TelemetryResponse]
)
def telemetry_history(
    limit: int = Query(
        default=100,
        ge=1,
        le=1000
    ),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    return TelemetryService.get_history(
        db,
        user["customer_id"],
        limit
    )