from datetime import datetime

from api.database.connection import get_connection
from api.database.actions import announcement_actions_db


class Announcement:
    def __init__(self, _id: str = None, text: str = None, created_time: str = None,
                 location: str = None, owner: int = None, language: str = None):

        self.id = _id
        self.text = text
        self.created_time = created_time
        self.location = location
        self.owner = owner
        self.language = language

    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def save(self):
        try:
            self._get_created_time_utc()
            with get_connection() as connection:
                announcement_actions_db.save_announcement(connection, self.text, self.created_time, self.location,
                self.owner, self.language)
            return f"Announcement was created !"
        except:
            return  f"Something went wrong, try again later"