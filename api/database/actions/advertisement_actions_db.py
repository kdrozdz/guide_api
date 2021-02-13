from api.database.cursor import get_cursor
from api.database.query.advertisement_query import INSERT_ADVERTISEMENT


def save_advertisement(connection, text, created_time, location, owner, language):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ADVERTISEMENT, (text, created_time, location, owner, language))
