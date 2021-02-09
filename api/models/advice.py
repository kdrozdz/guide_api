from datetime import datetime

from api.database.connection import get_connection
from api.database.actions import advice_actions_db

class Advice:
    def __init__(self, _id: str = None, text: str = None, created_time: str = None,
                owner: int = None, advertisement: int = None):

        self.id = _id
        self.text = text
        self.created_time = created_time
        self.owner = owner
        self.advertisement = advertisement

    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def save(self):
        try:
            self._get_created_time_utc()
            with get_connection() as connection:
                advice_actions_db.save_advice(connection,
                                                    self.text,
                                                    self.created_time,
                                                    self.owner,
                                                    self.advertisement)
            return f"Advice was created !"
        except:
            return f"Something went wrong, try again later"