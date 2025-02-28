from typing import Dict
from ..models.repositories.links_repository import LinksRepository
from ..models.repositories.trips_repository import TripsRepository

class LinkFinder:
    def __init__(self, link_repository: LinksRepository, trip_repository: TripsRepository) -> None:
        self.__link_repository = link_repository
        self.__trip_repository = trip_repository

    def find(self, trip_id) -> Dict:
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip: raise Exception("No trip found!")
            
            links = self.__link_repository.find_links_from_trip(trip_id)

            formatted_links = []
            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "url": link[2],
                    "title": link[3]
                })

            return {
                "body": { "links": formatted_links },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }