from .query.create_tables import (
    CREATE_USER_TABLE,
    CREATE_REPUTATION_TABLE,
    CREATE_ADVICE_TABLE,
    CREATE_ADVERTISEMENT_TABLE
)

from .cursor import get_cursor
from .connection import get_connection


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_USER_TABLE)
        cursor.execute(CREATE_ADVERTISEMENT_TABLE)
        cursor.execute(CREATE_ADVICE_TABLE)
        cursor.execute(CREATE_REPUTATION_TABLE)


def run_create_tables():
    with get_connection() as connection:
        create_tables(connection)
