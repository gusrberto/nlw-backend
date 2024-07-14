import uuid
from typing import Dict
from ..models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from ..models.repositories.participants_repository import ParticipantsRepository

class ParticipantCreator:
    def __init__(self, participants_repository: ParticipantsRepository, emails_repository: EmailsToInviteRepository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }

            self.__emails_repository.register_email(emails_infos)
            self.__participants_repository.register_participant(participant_infos)

            return {
                "body": { "participant_id": participant_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }