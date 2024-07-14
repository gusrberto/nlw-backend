from typing import Dict, Tuple, List
from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def register_activity(self, activity_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activities
                    (id, trip_id, email, occurs_at)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                activity_info["id"],
                activity_info["trip_id"],
                activity_info["title"],
                activity_info["occurs_at"]
            )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM activities WHERE trip_id = ?''', (trip_id,)
        )
        activities = cursor.fetchall()
        return activities