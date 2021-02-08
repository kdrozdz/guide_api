from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from api.schemas.advertisement import AdvertisementIn

from api.models.advertisement import  Advertisement

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

advertisement_router = APIRouter(dependencies=(Depends(oauth2_scheme),),
                                tags=["Advertisement"])


@advertisement_router.post("/create_advertisement/",)
async def user_create(model: AdvertisementIn) -> str:
    advertisement = Advertisement(**dict(model))
    return advertisement.save()