from ..models.user import User
from ..models.announcement import Announcement
from ..models.answer import Answer
from ..models.reputation import Reputation
from ..const import USERS_POPULATE, ANNOUNCEMENTS_POPULATE, ANSWER_POPULATE, REPUTATION_POPULATE


def create_users():
    for _obj in USERS_POPULATE:
        user = User(**_obj)
        user.save()


def create_announcement():
    for _obj in ANNOUNCEMENTS_POPULATE:
        announcements = Announcement(**_obj)
        announcements.save()


def create_answer():
    for _obj in ANSWER_POPULATE:
        answer = Answer(**_obj)
        answer.save()


def create_reputation():
    for _obj in REPUTATION_POPULATE:
        reputation = Reputation(**_obj)
        reputation.save()


def populate():
    create_users()
    create_announcement()
    create_answer()
    create_reputation()