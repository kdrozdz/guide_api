from ..models.user import User
from ..models.announcement import Announcement
from ..models.answer import Answer
from ..models.reputation import Reputation
from ..const import users_populate


def create_users():
    for _obj in users_populate:
        user = User(**_obj)
        user.save()

