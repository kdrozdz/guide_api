from fastapi import APIRouter, Depends
from api.authorization import oauth2_scheme

from api.schemas.advertisement import AdvertisementIn

from api.models.advertisement import Advertisement


advertisement_router = APIRouter(dependencies=(Depends(oauth2_scheme), ), tags=["Advertisement", ])


@advertisement_router.post("/create_advertisement/",)
async def create_advertisement(model: AdvertisementIn) -> str:
    advertisement = Advertisement(**dict(model))
    return advertisement.save()
