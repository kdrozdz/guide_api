from api.database.query.advice_query import INSERT_ADVICE
from api.database.cursor import get_cursor

def save_advice(connection, text, created_time, owner, advertisement):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ADVICE, (text, created_time, owner, advertisement))
