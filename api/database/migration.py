from .query.create_tables import (
    CREATE_USER_TABLE,
    CREATE_REPUTATION_TABLE,
    CREATE_ANSWER_TABLE,
    CREATE_ANNOUNCEMENT_TABLE
)

from .cursor import get_cursor
from .connection import get_connection


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_USER_TABLE)
        cursor.execute(CREATE_ANNOUNCEMENT_TABLE)
        cursor.execute(CREATE_ANSWER_TABLE)
        cursor.execute(CREATE_REPUTATION_TABLE)


def run_create_tables():
    with get_connection() as connection:
        create_tables(connection)
