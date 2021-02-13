from typing import List
from pydantic import BaseModel, Field

from .user import LocationIn
from ..schemas.answer import AnswerOut


class AnnouncementIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    language: str= Field(..., min_length=4, max_length=16)
    location: LocationIn
    owner: int

class AnnouncementOut(AnnouncementIn):
    id: str
    text: str
    created_time: str
    location: str
    language: str
    owner: str
    answers: List[AnswerOut]