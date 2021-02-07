from pydantic import BaseModel, EmailStr, Field
from aenum import StrEnum, extend_enum

from api.const import MAINLY_CITIES


class Location(StrEnum):
    pass


for key, value in MAINLY_CITIES:

    extend_enum(Location, key, key)


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    password: str = Field(..., min_length=4, max_length=16)
    location: Location
    email: EmailStr


class UserOut(BaseModel):
    email: EmailStr
