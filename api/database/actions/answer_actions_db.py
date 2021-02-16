from api.database.query.answer_query import DELETE_ANSWER, INSERT_ANSWER, GET_ALL_ANSWER_FOR_ANNOUNCEMENT
from api.database.cursor import get_cursor



def save_answer(connection, text, created_time, owner, announcement):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANSWER, (text, created_time, owner, announcement))


def get_all_answers_for_announcement(connection, _id: str):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_ALL_ANSWER_FOR_ANNOUNCEMENT, (_id,))
        response = cursor.fetchall()
        return response

def delete_answer(connection, _id:str):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_ANSWER, (_id))
