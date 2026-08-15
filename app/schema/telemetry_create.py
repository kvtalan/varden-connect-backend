from typing import Literal

from pydantic import BaseModel, Field


class TelemetryCreate(BaseModel):
    chassis_number: str = Field(
        min_length=5,
        max_length=50
    )

    soc: float = Field(
        ge=0,
        le=100
    )

    voltage: float = Field(
        gt=0
    )

    current: float

    battery_temp: float

    battery_health: float = Field(
        ge=0,
        le=100
    )

    motor_rpm: int = Field(
        ge=0
    )

    motor_temp: float

    torque: float = Field(
        ge=0
    )

    speed: float = Field(
        ge=0
    )

    gear: Literal[
        "Forward",
        "Neutral",
        "Reverse"
    ]

    mode: Literal[
        "Eco",
        "Normal",
        "Power"
    ]

    latitude: float = Field(
        ge=-90,
        le=90
    )

    longitude: float = Field(
        ge=-180,
        le=180
    )