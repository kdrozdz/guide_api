from api.database.connection import get_connection
from api.database.actions import user_actions_db

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User:
    def __init__(self, first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 location: str = None,
                 password: str = None,
                 _id: int = None):

        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.password = password

    def __repr__(self) -> str:
        return f"{self.email!r}, {self.location!r}, {self.id!r}"

    def _check_email_in_db(self) -> bool:
        with get_connection() as connection:
            return user_actions_db.check_email_in_db(connection, self.email)

    def _hash_password(self) -> None:
        self.password = pwd_context.hash(self.password)

    def _verify_password(self):
        with get_connection() as connection:
            hashed_password = user_actions_db.take_hashed_password_for_user(connection, self.email)
            return pwd_context.verify(self.password, hashed_password)

    def authenticate(self) -> bool:
        return self._verify_password()

    def save(self) -> str:
        if self._check_email_in_db():
            return f"Email: {self.email} is in DB"

        with get_connection() as connection:
            self._hash_password()
            user_actions_db.save_user(connection, self.first_name, self.last_name, self.email,
                                      self.location, self.password)
            return f"Email: {self.email} was created"
