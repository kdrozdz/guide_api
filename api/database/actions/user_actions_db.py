from api.database.cursor import get_cursor
from api.database.query.user_query import INSERT_USER, CHECK_USER_EMAIL, GET_USER_ALL_INFO,\
    GET_ALL_USERS_ORDER_BY, TAKE_HASHED_PASSWORD_FOR_USER_IN_DB


def save_user(connection, first_name, last_name, email, location, password) -> None:
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_USER, (first_name, last_name, email, location, password))


def check_email_in_db(connection, email:str) -> bool:
    with get_cursor(connection) as cursor:
        cursor.execute(CHECK_USER_EMAIL, (email,))
        response = cursor.fetchone()
        return response


def take_hashed_password_for_user(connection, email:str) -> str:
    with get_cursor(connection) as cursor:
        cursor.execute(TAKE_HASHED_PASSWORD_FOR_USER_IN_DB, (email,))
        response = cursor.fetchone()[0]
        return response


def get_user_all_info(connection, email: str) -> list:
    with get_cursor(connection) as cursor:
        cursor.execute(GET_USER_ALL_INFO, (email,))
        response = cursor.fetchone()
        return response


def get_all_users_order_by(connection, order_by: str):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_ALL_USERS_ORDER_BY, (order_by,))
        response = cursor.fetchall()
        return response
