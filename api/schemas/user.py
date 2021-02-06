from pydantic import BaseModel, EmailStr, Field
from aenum import Enum, IntEnum, extend_enum

from api.const import MAINLY_CITIES


"""id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR,
    loaction VARCHAR,
    hashed_password VARCHAR,
    profile SMALLINT,
    disabled boolean);"""


# from aenum import IntEnum
#
# class CombinedEnum(IntEnum):
#     """ doc string """
#     _ignore_ = 'member cls'
#     cls = vars()
#     for member in chain(list(FirstEnumClass), list(SecondEnumClass)):
#         cls[member.name] = member.value

class Location(IntEnum):
    pass
for key, value in MAINLY_CITIES:
    extend_enum(Location, value, key)


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    password: str = Field(..., min_length=4, max_length=16)
    loaction: Location
    email: EmailStr

class UserOut(BaseModel):
    loaction: Location
