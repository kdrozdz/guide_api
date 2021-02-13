from datetime import datetime

from api.database.connection import get_connection
from api.database.actions import advertisement_actions_db


class Advertisement:
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
                advertisement_actions_db.save_advertisement(connection, self.text, self.created_time, self.location,
                self.owner, self.language)
            return f"Advertisement was created !"
        except:
            return  f"Something went wrong, try again later"