from datetime import datetime

from pydantic import BaseModel


class BatteryData(BaseModel):
    soc: int
    voltage: float
    current: float
    temperature: float
    health: int


class MotorData(BaseModel):
    rpm: int
    temperature: float
    torque: float


class VehicleData(BaseModel):
    speed: float
    gear: str
    mode: str


class LocationData(BaseModel):
    latitude: float
    longitude: float


class TelemetryResponse(BaseModel):
    tractor_status: str
    last_updated: datetime

    battery: BatteryData
    motor: MotorData
    vehicle: VehicleData
    location: LocationData