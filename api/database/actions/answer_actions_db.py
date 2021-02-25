from pydantic import EmailStr

from api.database.query.answer_query import DELETE_ANSWER, INSERT_ANSWER, GET_ALL_ANSWER_FOR_ANNOUNCEMENT, UPDATE_ANSWER
from api.database.cursor import get_cursor


def save_answer(connection, text: str, created_time: str, owner: EmailStr, announcement: int):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANSWER, (text, created_time, owner, announcement))


def get_all_answers_for_announcement(connection, _id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_ALL_ANSWER_FOR_ANNOUNCEMENT, (_id,))
        response = cursor.fetchall()
        return response


def delete_answer(connection, _id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_ANSWER, (_id))


def update_answer(connection, _id: int, text: str, created_time: str):
    with get_cursor(connection) as cursor:
        cursor.execute(UPDATE_ANSWER, (created_time, text, _id))