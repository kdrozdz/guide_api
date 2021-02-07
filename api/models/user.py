from api.database.connection import get_connection
from api.database.actions import user_actions_db

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User:
    def __init__(self, first_name: str, last_name: str, email: str, location: str, password: str, _id: int = None):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.password = password

    def __repr__(self) -> str:
        return f"{self.email!r}, {self.location!r}, {self.id!r}"

    """id SERIAL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        email VARCHAR,
        loaction VARCHAR,
        hashed_password VARCHAR,
        profile SMALLINT,
        disabled boolean);"""

    def _hash_password(self):
        self.password = pwd_context.hash(self.password)

    def save(self):
        with get_connection() as connection:
            self._hash_password()
            user_actions_db.save(connection, self.first_name, self.last_name, self.email, self.location, self.password)
