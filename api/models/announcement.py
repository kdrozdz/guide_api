from datetime import datetime

from ..database.connection import get_connection
from ..database.actions import announcement_actions_db, answer_actions_db
from ..models.mapper import MapperObj
from ..mapping_schemas.mapping_schemas import GET_SPECIFIC_ANNOUNCEMENT,\
    GET_ALL_ANSWERS_FOR_ANNOUNCEMENT, GET_LIST_OF_ANNOUNCEMENT


class Announcement:
    def __init__(self, _id: str = None, text: str = None, created_time: str = None,
                 location: str = None, owner: int = None, language: str = None):

        self.id = _id
        self.text = text
        self.created_time = created_time
        self.location = location
        self.owner = owner
        self.language = language
        self.announcement_for_db = None
        self.answer_for_db = None


    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def get_specific_announcement(self):
        with get_connection() as connection:
            self.announcement_for_db = announcement_actions_db.get_specific_announcement(connection, self.id)
            self.answer_for_db = answer_actions_db.get_all_answers_for_announcement(connection, self.id)

        announcement_mapper_obj = MapperObj(self.announcement_for_db, GET_SPECIFIC_ANNOUNCEMENT, location_name=True)
        answer_mapper_obj = MapperObj(self.answer_for_db, GET_ALL_ANSWERS_FOR_ANNOUNCEMENT)

        if self.announcement_for_db:
            announcement_dict = announcement_mapper_obj.get_specifict_dict()
            announcement_dict["answers"] = answer_mapper_obj.get_list_of_dict()
            return announcement_dict
        return []

    def get_list_of_announcement_location_or_owner(self, value_location_or_owner, location_or_owner):
        with get_connection() as connection:
           self.announcement_for_db = announcement_actions_db.get_list_of_announcement(
               connection, value_location_or_owner, location_or_owner)

        if self.announcement_for_db:
            announcement_mapper_obj = MapperObj(self.announcement_for_db, GET_LIST_OF_ANNOUNCEMENT, location_name=True)
            if len(self.announcement_for_db) > 1:
                return announcement_mapper_obj.get_list_of_dict()
            else:
                return announcement_mapper_obj.get_specifict_dict()
        else:
            return []

    def delete_announcement(self):
        with get_connection() as connection:
            announcement_actions_db.delete_announcement(connection, self.id)
        return f"Announcement has been deleted"

    def save(self):
        self._get_created_time_utc()
        with get_connection() as connection:
            announcement_actions_db.save_announcement(connection, self.text, self.created_time, self.location,
                self.owner, self.language)
        return f"Announcement was created !"
