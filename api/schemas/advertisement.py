from pydantic import BaseModel, Field
from .user import LocationIn


class AdvertisementIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    language: str= Field(..., min_length=4, max_length=16)
    location: LocationIn
    owner: int
