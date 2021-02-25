from datetime import datetime

from pydantic import EmailStr

from ..database.connection import get_connection
from ..database.actions import announcement_actions_db, answer_actions_db
from ..models.mapper import MapperObj
from ..mapping_schemas.mapping_schemas import GET_SPECIFIC_ANNOUNCEMENT,\
    GET_ALL_ANSWERS_FOR_ANNOUNCEMENT, GET_LIST_OF_ANNOUNCEMENT
from ..schemas.announcement import ValueLocationOrOwner, LocationOrOwner


class Announcement:
    def __init__(self, _id: int = None, text: str = None, created_time: str = None,
                 location: str = None, owner: EmailStr = None, language: str = None):

        self.id = _id
        self.text = text
        self.created_time = created_time
        self.location = location
        self.owner = owner
        self.language = language
        self.announcement_for_db = None
        self.answer_for_db = []


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
        return self.announcement_for_db


    def get_list_of_announcement_location_or_owner(self, value_location_or_owner: ValueLocationOrOwner,
                                                   location_or_owner: LocationOrOwner):
        with get_connection() as connection:
           self.announcement_for_db = announcement_actions_db.get_list_of_announcement(
               connection, value_location_or_owner, location_or_owner)
        if self.announcement_for_db:
            announcement_mapper_obj = MapperObj(self.announcement_for_db, GET_LIST_OF_ANNOUNCEMENT, location_name=True)
            return announcement_mapper_obj.get_list_of_dict()
        return []


    def search_announcement_by_language_location(self):
        if not self.language and not self.location:
            return []

        with get_connection() as connection:
            self.announcement_for_db = announcement_actions_db.search_announcement_by_language_location(
                connection, self.location, self.language)
        if self.announcement_for_db:
            announcement_mapper_obj = MapperObj(self.announcement_for_db, GET_LIST_OF_ANNOUNCEMENT, location_name=True)
            return announcement_mapper_obj.get_list_of_dict()
        return []

    def delete_announcement(self):
        with get_connection() as connection:
            announcement_actions_db.delete_announcement(connection, self.id)
        return f"Announcement has been deleted"

    def announcement_update_row(self):
        self._get_created_time_utc()
        with get_connection() as connection:
            announcement_actions_db.update_annoucement(connection, self.id, self.location, self.text, self.language,
                                                       self.created_time)
        return f"Announcement has been updated"

    def save(self):
        self._get_created_time_utc()
        with get_connection() as connection:
            announcement_actions_db.save_announcement(connection, self.text, self.created_time, self.location,
                self.owner, self.language)
        return f"Announcement was created !"
