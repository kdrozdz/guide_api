from api.database.cursor import get_cursor
from api.database.query.announcement_query import INSERT_ANNOUNCEMENT


def save_announcement(connection, text, created_time, location, owner, language):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANNOUNCEMENT, (text, created_time, location, owner, language))
