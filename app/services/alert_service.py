from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository


class AlertService:

    LOW_BATTERY_THRESHOLD = 15
    HIGH_BATTERY_TEMP = 60
    HIGH_MOTOR_TEMP = 90
    OVERSPEED_LIMIT = 40

    @staticmethod
    def check_alerts(db, tractor_id, telemetry):

        # Low Battery
        if telemetry.soc < AlertService.LOW_BATTERY_THRESHOLD:
            AlertRepository.create(
                db,
                Alert(
                    tractor_id=tractor_id,
                    title="Low Battery",
                    message=f"Battery SOC is {telemetry.soc}%",
                    severity="WARNING"
                )
            )

        # Battery Over Temperature
        if telemetry.battery_temp > AlertService.HIGH_BATTERY_TEMP:
            AlertRepository.create(
                db,
                Alert(
                    tractor_id=tractor_id,
                    title="Battery Over Temperature",
                    message=f"Battery temperature is {telemetry.battery_temp}°C",
                    severity="CRITICAL"
                )
            )

        # Motor Over Temperature
        if telemetry.motor_temp > AlertService.HIGH_MOTOR_TEMP:
            AlertRepository.create(
                db,
                Alert(
                    tractor_id=tractor_id,
                    title="Motor Over Temperature",
                    message=f"Motor temperature is {telemetry.motor_temp}°C",
                    severity="CRITICAL"
                )
            )

        # Overspeed
        if telemetry.speed > AlertService.OVERSPEED_LIMIT:
            AlertRepository.create(
                db,
                Alert(
                    tractor_id=tractor_id,
                    title="Overspeed",
                    message=f"Vehicle speed is {telemetry.speed} km/h",
                    severity="WARNING"
                )
            )