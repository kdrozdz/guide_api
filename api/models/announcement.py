from datetime import datetime

from api.database.connection import get_connection
from api.database.actions import announcement_actions_db
from api.models.mapper import MapperObj
from api.mapping_schemas.mapping_schemas import GET_SPECIFIC_ANNOUNCEMENT

class Announcement:
    def __init__(self, _id: str = None, text: str = None, created_time: str = None,
                 location: str = None, owner: int = None, language: str = None):

        self.id = _id
        self.text = text
        self.created_time = created_time
        self.location = location
        self.owner = owner
        self.language = language
        self.response_for_db = None

    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def get_specific_announcement(self):
        try:
            with get_connection() as connection:
                self.response_for_db = announcement_actions_db.get_specific_announcement(connection, self.id)
            mapper = MapperObj(self.response_for_db, GET_SPECIFIC_ANNOUNCEMENT, location_name=True)
            return mapper.get_specifict_dict()
        except:
            pass

    def save(self):
        try:
            self._get_created_time_utc()
            with get_connection() as connection:
                announcement_actions_db.save_announcement(connection, self.text, self.created_time, self.location,
                self.owner, self.language)
            return f"Announcement was created !"
        except:
            return  f"Something went wrong, try again later"