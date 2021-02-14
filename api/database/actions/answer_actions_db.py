from api.database.query.answer_query import INSERT_ANSWER, GET_ALL_ANSWER_FOR_ANNOUNCEMENT
from api.database.cursor import get_cursor

def save_answer(connection, text, created_time, owner, announcement):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANSWER, (text, created_time, owner, announcement))

def get_all_answers_for_announcement(connection, id):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_ALL_ANSWER_FOR_ANNOUNCEMENT, (id,))
        response = cursor.fetchall()
        return response