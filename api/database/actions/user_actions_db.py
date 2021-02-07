from api.database.cursor import get_cursor
from api.database.query.user_query import INSERT_USER, CHECK_USER_EMAIL, TAKE_HASHED_PASSWORD_FOR_USER_IN_DB


def save(connection, first_name, last_name, email, loaction, password):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_USER, (first_name, last_name, email, loaction, password))

def check_email_in_db(connection, email):
    with get_cursor(connection) as cursor:
        cursor.execute(CHECK_USER_EMAIL, (email,))
        return cursor.fetchone()

def take_hashed_password_for_user(connection, email):
    with get_cursor(connection) as cursor:
        cursor.execute(TAKE_HASHED_PASSWORD_FOR_USER_IN_DB, (email,))
        return cursor.fetchone()
