from fastapi import APIRouter, Depends

from api.schemas.reputation import ReputationIn
from api.models.reputation import Reputation

from api.authorization import oauth2_scheme

reputation_router = APIRouter(tags=["Reputation",], dependencies=(Depends(oauth2_scheme),))


@reputation_router.post("/create_reputation/")
def user_create(model: ReputationIn) -> str:
    reputation = Reputation(**dict(model))
    return reputation.save()
