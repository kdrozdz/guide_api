from datetime import datetime

from api.database.connection import get_connection
from api.database.actions import answer_actions_db


class Answer:
    def __init__(self, _id: str = None, text: str = None, created_time: str = None, owner: int = None,
                 announcement: int = None):
        self.id = _id
        self.text = text
        self.created_time = created_time
        self.owner = owner
        self.announcement = announcement

    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def save(self):
        try:
            self._get_created_time_utc()
            with get_connection() as connection:
                answer_actions_db.save_answer(connection, self.text, self.created_time, self.owner, self.announcement)
            return f"Answer was created !"
        except:
            return f"Something went wrong, try again later"