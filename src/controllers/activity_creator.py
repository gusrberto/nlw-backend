import uuid
from typing import Dict
from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
    def __init__(self, activities_repository: ActivitiesRepository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, trip_id) -> Dict:
        try:
            activity_id = str(uuid.uuid4())
            activities_info = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"]
            }

            self.__activities_repository.register_activity(activities_info)

            return {
                "body": { "activity_id": activity_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }            