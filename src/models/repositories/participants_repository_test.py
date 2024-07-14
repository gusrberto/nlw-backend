import pytest
import uuid
from datetime import datetime, timedelta
from .participants_repository import ParticipantsRepository
from .trips_repository import TripsRepository
from .emails_to_invite_repository import EmailsToInviteRepository
from ..settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_register_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    trip_repository = TripsRepository(conn)
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    # Mock Trip
    trips_infos = {
        "id": trip_id,
        "destination": "local teste",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Fdp",
        "owner_email": "fdp_pnc@gmail.com"
    }

    trip_repository.create_trip(trips_infos)

    # Mock Email
    email_trips_infos = {
        "id": emails_to_invite_id,
        "trip_id": trip_id,
        "email": "emersonjb17@gmail.com"
    }

    emails_to_invite_repository.register_email(email_trips_infos)

    participant_info = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "José"
    }

    participants_repository.register_participant(participant_info)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_repository.find_participants_from_trip(trip_id)

@pytest.mark.skip(reason="interacao com o banco")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_repository.update_participant_status(participant_id)
