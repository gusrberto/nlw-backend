from typing import Dict
import uuid
from ..models.repositories.links_repository import LinksRepository

class LinkCreator:
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_info = {
                "link": body["url"],
                "title": body["title"],
                "id": link_id,
                "trip_id": trip_id
            }
            self.__link_repository.register_link(link_info)

            return {
                "body": { "link_id": link_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }