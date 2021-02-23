from pydantic import EmailStr

from api.database.cursor import get_cursor
from api.database.query.announcement_query import INSERT_ANNOUNCEMENT, GET_SPECIFIC_ANNOUNCEMENT,\
    GET_LIST_OF_ANNOUNCEMENT_LOCATION, GET_LIST_OF_ANNOUNCEMENT_OWNER, DELETE_ANNOUNCEMENT, UPDATE_ANNOUNCEMENT
from api.schemas.announcement import ValueLocationOrOwner, LocationOrOwner


def save_announcement(connection, text: str, created_time: str, location: str, owner: EmailStr, language: str):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_ANNOUNCEMENT, (text, created_time, location, owner, language))


def get_specific_announcement(connection, _id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(GET_SPECIFIC_ANNOUNCEMENT, (_id,))
        response = cursor.fetchone()
        return response


def get_list_of_announcement(connection, value: ValueLocationOrOwner, location_or_owner: LocationOrOwner):
    def switch_sql_quer(_type):
        options = {
            "owner": GET_LIST_OF_ANNOUNCEMENT_OWNER,
            "location": GET_LIST_OF_ANNOUNCEMENT_LOCATION,
        }
        return options[_type]

    with get_cursor(connection) as cursor:
        cursor.execute(switch_sql_quer(location_or_owner), (value,))
        response = cursor.fetchall()
        return response


def delete_announcement(connection, _id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_ANNOUNCEMENT, (_id,))


def update_annoucement(connection, _id:  int, location: str, text: str, language: str, created_time: str):
    with get_cursor(connection) as cursor:
        cursor.execute(UPDATE_ANNOUNCEMENT, (created_time, language, text, location, _id))
