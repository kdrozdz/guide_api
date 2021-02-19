from typing import List
from fastapi import APIRouter, Depends, HTTPException

from ..authorization import oauth2_scheme
from ..schemas.user import UserEmail
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
        raise HTTPException(status_code=MESSAGE_400 , detail="Check your request data ")

@reputation_router.post("/get_reputations/")
def get_reputations(email: UserEmail) -> List[ReputationOut]:
    # try:
        reputation = Reputation(to_user=email)
        return reputation.get_reputations()
    # except:
    #     raise HTTPException(status_code=MESSAGE_400 , detail="Check your request data ")