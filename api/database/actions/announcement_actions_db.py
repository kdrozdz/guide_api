from api.database.cursor import get_cursor
from api.database.query.announcement_query import INSERT_ANNOUNCEMENT, GET_SPECIFIC_ANNOUNCEMENT,\
    GET_LIST_OF_ANNOUNCEMENT_LOCATION, GET_LIST_OF_ANNOUNCEMENT_OWNER, DELETE_ANNOUNCEMENT, UPDATE_ANNOUNCEMENT


def save_announcement(connection, text, created_time, location, owner, language):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANNOUNCEMENT, (text, created_time, location, owner, language))


def get_specific_announcement(connection, _id: str):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_SPECIFIC_ANNOUNCEMENT, (_id,))
        response = cursor.fetchone()
        return response


def get_list_of_announcement(connection, value, location_or_owner):

    def switch_sql_quer(type):
        options = {
            "owner": GET_LIST_OF_ANNOUNCEMENT_OWNER,
            "location": GET_LIST_OF_ANNOUNCEMENT_LOCATION,
        }
        return options[type]

    with get_cursor(connection) as cursor:
        cursor.execute(switch_sql_quer(location_or_owner), (value,))
        response = cursor.fetchall()
        return response

def delete_announcement(connection, _id):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_ANNOUNCEMENT, (_id))

def update_annoucement(connection, _id, location, text, language, created_time):
    with get_cursor(connection) as cursor:
        cursor.execute(UPDATE_ANNOUNCEMENT, (created_time, language, text, location, _id))