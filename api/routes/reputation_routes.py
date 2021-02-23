from typing import List
from fastapi import APIRouter, HTTPException, status
from pydantic import EmailStr

from ..authorization import oauth2_scheme
from ..models.reputation import Reputation
from ..schemas.reputation import ReputationIn, ReputationOut
from ..const import MESSAGE_400


reputation_router = APIRouter(tags=["Reputation", ])


@reputation_router.post("/create_reputation/")
def create_reputation(model: ReputationIn) -> str:
    try:
        reputation = Reputation(**dict(model))
        return reputation.save()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)


@reputation_router.post("/get_reputations/")
def get_reputations(email: EmailStr) -> List[ReputationOut]:
    try:
        reputation = Reputation(to_user=email)
        return reputation.get_reputations()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)
