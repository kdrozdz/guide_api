from pydantic import EmailStr

from api.database.query.reputation import INSERT_REPUTATION, CHECK_NO_REPEAT_REPUTATION_FOR_USER, UPDATE_REPUTATION, \
    GET_REPUTATIONS_FOR_USER
from api.database.cursor import get_cursor


def save_reputation(connection, from_user: EmailStr, to_user: EmailStr, created_time: str, rating: float, text: str):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_REPUTATION, (from_user, to_user, created_time, rating, text))


def check_user_give_feedback(connection, from_user: EmailStr, to_user: EmailStr):
    with get_cursor(connection) as cursor:
        cursor.execute(CHECK_NO_REPEAT_REPUTATION_FOR_USER, (from_user, to_user))
        response = cursor.fetchone()
        return bool(response)


def update_feedback(connection, rating: float, from_user: EmailStr, to_user: EmailStr):
    with get_cursor(connection) as cursor:
        cursor.execute(UPDATE_REPUTATION, (rating, from_user, to_user))


def get_reputations_for_user(connection, to_user: EmailStr,):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_REPUTATIONS_FOR_USER, (to_user,))
        response = cursor.fetchall()
        return response
