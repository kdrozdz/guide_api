from typing import List, Union
from enum import Enum

from pydantic import BaseModel, Field, EmailStr

from .user import LocationIn
from ..schemas.answer import AnswerOut


class AnnouncementListOut(BaseModel):
    location: str
    owner: str
    language: str

class AnnouncementIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    language: str= Field(..., min_length=4, max_length=16)
    location: LocationIn
    owner: str


class AnnouncementOut(AnnouncementIn):
    id: int
    created_time: str
    answers: List[AnswerOut]


class LocationOrOwner (str, Enum):
    location = "location"
    owner = "owner"


class ValueLocationOrOwner (BaseModel):
    value: Union[EmailStr, LocationIn]