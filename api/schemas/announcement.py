from typing import List, Union
from enum import Enum

from aenum import StrEnum, extend_enum
from pydantic import BaseModel, Field, EmailStr

from .user import LocationIn
from ..schemas.answer import AnswerOut

from api.const import MAINLY_CITIES_BLANK


class LocationInBlank(StrEnum):
    pass


for key, value in MAINLY_CITIES_BLANK:
    extend_enum(LocationInBlank, key, key)


class AnnouncementListOut(BaseModel):
    location: str
    owner: EmailStr
    language: str
    id: int

class AnnouncementIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    language: str= Field(..., min_length=4, max_length=16)
    location: LocationIn
    owner: EmailStr


class AnnouncementUpdateIn(AnnouncementIn):
    id: str
    created_time: str
    location: str


class AnnouncementOut(AnnouncementUpdateIn):
    answers: List[AnswerOut]


class LocationOrOwner (str, Enum):
    location = "location"
    owner = "owner"


class ValueLocationOrOwner (BaseModel):
    value: Union[EmailStr, LocationIn]


class LanguageLocation(BaseModel):
    language: str = Field(None, max_length=16)
    location: LocationInBlank