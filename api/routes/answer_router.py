from fastapi import APIRouter, Depends, HTTPException

from api.authorization import oauth2_scheme
from api.schemas.answer import AnswerIn
from api.models.answer import Answer


answer_router = APIRouter(tags=["Answer", ], dependencies=(Depends(oauth2_scheme),))


@answer_router.post("/create_answer/")
async def create_answer(model: AnswerIn) -> str:
    try:
        answer = Answer(**dict(model))
        return answer.save()
    except:
        raise HTTPException(status_code=400 , detail="Check your request data ")