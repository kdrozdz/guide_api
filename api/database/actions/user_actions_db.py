from api.database.cursor import get_cursor
from api.database.query.user_query import INSERT_USER


def save(connection, first_name, last_name, email, loaction, password):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_USER, (first_name, last_name, email, loaction, password))
