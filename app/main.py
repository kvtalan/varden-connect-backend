from fastapi import FastAPI

from app.database import Base, engine

# Models
from app.models.customer import Customer
from app.models.tractor import Tractor
from app.models.otp import OTP
from app.models.telemetry import Telemetry
from app.models.alert import Alert
from app.models.trip import Trip

# Routes
from app.routes.auth import router as auth_router
from app.routes.tractor import router as tractor_router
from app.routes.user import router as user_router
from app.routes.telemetry import router as telemetry_router
from app.routes.alert import router as alert_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Varden Connect API"
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    tractor_router,
    prefix="/tractor",
    tags=["Tractor"]
)

app.include_router(
    user_router,
    tags=["User"]
)

app.include_router(
    telemetry_router,
    prefix="/tractor",
    tags=["Telemetry"]
)

app.include_router(
    alert_router
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Varden Connect API"
    }