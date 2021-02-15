from fastapi import APIRouter, Depends, HTTPException

from ..authorization import oauth2_scheme
from ..models.answer import Answer
from ..schemas.answer import AnswerIn
from ..const import MESSAGE_400

answer_router = APIRouter(tags=["Answer", ], dependencies=(Depends(oauth2_scheme),))


@answer_router.post("/create_answer/")
async def create_answer(model: AnswerIn) -> str:
    try:
        answer = Answer(**dict(model))
        return answer.save()
    except:

        raise HTTPException(status_code=400 , detail=MESSAGE_400)