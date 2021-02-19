from datetime import datetime

from ..database.connection import get_connection
from ..database.actions.reputation_actions_db import  check_user_give_feedback, save_reputation, update_feedback,\
    get_reputations_for_user
from ..models.mapper import MapperObj
from ..schemas.user import UserEmail
from  ..mapping_schemas.mapping_schemas import GET_REPUTATIONS_FOR_USER

class Reputation:
    def __init__(self, _id: str = None, from_user: int = None, to_user: UserEmail = None,
                 created_time: str = None, rating: int = None, text: str = None):
        self.id = _id
        self.from_user = from_user
        self.to_user = to_user
        self.created_time = created_time
        self.rating = rating
        self.text = text
        self.answer_from_db = []

    def _get_created_time_utc(self):
        self.created_time = str(datetime.utcnow())

    def _check_different_from_user_to_user(self):
        return self.to_user == self.from_user

    def _check_user_gave_feedback(self):
        with get_connection() as connection:
            return check_user_give_feedback(connection, self.from_user, self.to_user)

    def save(self):
        if self._check_different_from_user_to_user():
            return f"You can't give a feedback to yourself"
        if self._check_user_gave_feedback():
            with get_connection() as connection:
                update_feedback(connection, self.rating, self.from_user, self.to_user)
                return f"Your opinion was update"
        self._get_created_time_utc()
        with get_connection() as connection:
            save_reputation(connection, self.from_user, self.to_user, self.created_time, self.rating, self.text)
            return f"Your feedback was created !"

    def get_reputations(self):
        with get_connection() as connection:
            self.answer_from_db = get_reputations_for_user(connection, self.to_user.email)

        if self.answer_from_db:
            all_reputations = MapperObj(self.answer_from_db, GET_REPUTATIONS_FOR_USER)
            return all_reputations.get_list_of_dict()
        return []