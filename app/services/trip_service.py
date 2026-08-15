from app.models.trip import Trip
from app.repositories.trip_repository import TripRepository


class TripService:

    START_SPEED = 1

    @staticmethod
    def start_trip(db, tractor_id, telemetry):

        trip = Trip(
            tractor_id=tractor_id,

            start_soc=telemetry.soc,

            start_latitude=telemetry.latitude,
            start_longitude=telemetry.longitude,

            end_latitude=telemetry.latitude,
            end_longitude=telemetry.longitude,

            max_speed=telemetry.speed,
            avg_speed=telemetry.speed
        )

        return TripRepository.create(
            db,
            trip
        )

    @staticmethod
    def update_trip(db, trip, telemetry):

        trip.end_soc = telemetry.soc

        trip.end_latitude = telemetry.latitude
        trip.end_longitude = telemetry.longitude

        if telemetry.speed > trip.max_speed:
            trip.max_speed = telemetry.speed

        trip.avg_speed = (
            trip.avg_speed + telemetry.speed
        ) / 2

        return TripRepository.update(
            db,
            trip
        )

    @staticmethod
    def process_telemetry(
        db,
        tractor_id,
        telemetry
    ):

        active_trip = TripRepository.get_active_trip(
            db,
            tractor_id
        )

        if active_trip is None:

            if telemetry.speed >= TripService.START_SPEED:

                return TripService.start_trip(
                    db,
                    tractor_id,
                    telemetry
                )

            return None

        return TripService.update_trip(
            db,
            active_trip,
            telemetry
        )