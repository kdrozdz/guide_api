from fastapi import APIRouter, Depends

from api.authorization import oauth2_scheme
from api.schemas.advice import AdviceIn
from api.models.advice import Advice


advice_router = APIRouter(tags=["Advice",], dependencies=(Depends(oauth2_scheme),))


@advice_router.post("/create_advice/")
async def user_create(model: AdviceIn) -> str:
    advice = Advice(**dict(model))
    return advice.save()