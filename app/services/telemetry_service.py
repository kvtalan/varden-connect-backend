from app.models.telemetry import Telemetry
from app.repositories.telemetry_repository import TelemetryRepository
from app.repositories.tractor_repository import TractorRepository
from app.services.alert_service import AlertService
from app.services.trip_service import TripService


class TelemetryService:

    @staticmethod
    def create(db, telemetry_data):

        tractor = TractorRepository.get_by_chassis_number(
            db,
            telemetry_data.chassis_number
        )

        if tractor is None:
            return None

        telemetry = Telemetry(
            tractor_id=tractor.id,
            soc=telemetry_data.soc,
            voltage=telemetry_data.voltage,
            current=telemetry_data.current,
            battery_temp=telemetry_data.battery_temp,
            battery_health=telemetry_data.battery_health,
            motor_rpm=telemetry_data.motor_rpm,
            motor_temp=telemetry_data.motor_temp,
            torque=telemetry_data.torque,
            speed=telemetry_data.speed,
            gear=telemetry_data.gear,
            mode=telemetry_data.mode,
            latitude=telemetry_data.latitude,
            longitude=telemetry_data.longitude,
        )

        saved_telemetry = TelemetryRepository.create(
        db,
         telemetry
        )

        AlertService.check_alerts(
    db=db,
    tractor_id=tractor.id,
    telemetry=saved_telemetry
)

        TripService.process_telemetry(
    db=db,
    tractor_id=tractor.id,
    telemetry=saved_telemetry
)

        return saved_telemetry


    @staticmethod
    def get_live_data(db, customer_id):

        tractor = TractorRepository.get_by_customer_id(
            db,
            customer_id
        )

        if not tractor:
            return None

        return TelemetryRepository.get_latest_by_tractor_id(
            db,
            tractor.id
        )

    @staticmethod
    def get_history(
        db,
        customer_id,
        limit: int = 100
    ):

        tractor = TractorRepository.get_by_customer_id(
            db,
            customer_id
        )

        if tractor is None:
            return []

        return TelemetryRepository.get_history_by_tractor_id(
            db,
            tractor.id,
            limit
        )