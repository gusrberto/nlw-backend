from typing import Dict
from ..models.repositories.trips_repository import TripsRepository

class TripConfirmer:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def confirm(self, trip_id) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip: raise Exception("No trip found!")
                
            self.__trips_repository.update_trip_status(trip_id)

            return { "body": None, "status_code": 204 }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }