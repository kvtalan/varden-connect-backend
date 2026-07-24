from fastapi import FastAPI

from app.database import Base, engine
from app.models.customer import Customer
from app.models.tractor import Tractor
from app.routes.auth import router as auth_router
from app.models.otp import OTP
from app.routes.tractor import router as tractor_router
from app.routes.user import router as user_router



Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(
    tractor_router, prefix="/tractor", tags=["Tractor"])
app.include_router(
    user_router,
    tags=["User"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Varden Connect API"
    }

