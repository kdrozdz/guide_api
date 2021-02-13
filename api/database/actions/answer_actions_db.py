from api.database.query.answer_query import INSERT_ANSWER
from api.database.cursor import get_cursor

def save_answer(connection, text, created_time, owner, announcement):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANSWER, (text, created_time, owner, announcement))
