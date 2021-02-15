
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.reputation import ReputationIn
from api.models.reputation import Reputation

from api.authorization import oauth2_scheme

reputation_router = APIRouter(tags=["Reputation", ], dependencies=(Depends(oauth2_scheme),))


@reputation_router.post("/create_reputation/")
def create_reputation(model: ReputationIn) -> str:
    try:
        reputation = Reputation(**dict(model))
        return reputation.save()
    except:
        raise HTTPException(status_code=400 , detail="Check your request data ")