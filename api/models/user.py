from passlib.context import CryptContext

from ..database.connection import get_connection
from ..database.actions.user_actions_db import check_email_in_db, get_all_users_order_by, get_user_all_info, save_user, \
    take_hashed_password_for_user
from ..mapping_schemas import mapping_schemas
from ..models.mapper import MapperObj
from ..schemas.user import UserEmail


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, first_name: str = None,
                 last_name: str = None,
                 email: UserEmail = None,
                 location: str = None,
                 password: str = None,
                 _id: int = None):

        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.password = password
        self.users_response_from_db = None
        self.announcement_response_from_db = None
        self.reputation_response_from_db = None


    def get_all_users_order_by(self, order_by='location'):
        with get_connection() as connection:
            self.users_response_from_db = get_all_users_order_by(connection, order_by)
        all_users = MapperObj(self.users_response_from_db, mapping_schemas.GET_ALL_USERS_ORDER_BY, location_name=True)
        return all_users.get_list_of_dict()

    def __repr__(self) -> str:
        return f"{self.email!r}, {self.location!r}, {self.id!r}"

    def _check_email_in_db(self) -> bool:
        with get_connection() as connection:
            return bool(check_email_in_db(connection, self.email))

    def _hash_password(self) -> None:
        self.password = pwd_context.hash(self.password)

    def _verify_password(self):
        with get_connection() as connection:
            hashed_password = take_hashed_password_for_user(connection, self.email)
            return pwd_context.verify(self.password, hashed_password)

    def get_user_all_info(self):
        with get_connection() as connection:
            self.users_response_from_db = get_user_all_info(connection, self.email)
        user_all_info = MapperObj(self.users_response_from_db, mapping_schemas.GET_USER_ALL_INFO, location_name=True)
        return user_all_info.get_specifict_dict()

    def authenticate(self) -> bool:
        return self._check_email_in_db() and self._verify_password()

    def save(self) -> str:
        if self._check_email_in_db():
            return f"Email: {self.email} is in DB"

        with get_connection() as connection:
            self._hash_password()
            save_user(connection, self.first_name, self.last_name, self.email, self.location, self.password)
            return f"Email: {self.email} was created"
