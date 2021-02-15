from fastapi import APIRouter, Depends, HTTPException

from ..authorization import oauth2_scheme
from ..models.reputation import Reputation
from ..schemas.reputation import ReputationIn
from ..const import MESSAGE_400

reputation_router = APIRouter(tags=["Reputation", ], dependencies=(Depends(oauth2_scheme),))


@reputation_router.post("/create_reputation/")
def create_reputation(model: ReputationIn) -> str:
    try:
        reputation = Reputation(**dict(model))
        return reputation.save()
    except:
        raise HTTPException(status_code=MESSAGE_400 , detail="Check your request data ")