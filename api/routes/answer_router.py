from fastapi import APIRouter, status, HTTPException

from ..authorization import oauth2_scheme
from ..models.answer import Answer
from ..schemas.answer import AnswerIn, AnswerPut
from ..const import MESSAGE_400

answer_router = APIRouter(tags=["Answer", ])


@answer_router.post("/create_answer/")
async def create_answer(model: AnswerIn) -> str:
    try:
        answer = Answer(**dict(model))
        return answer.save()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)


@answer_router.delete("/delete_answer/")
async def delete_answer(answer_id: int) -> str:
    try:
        answer = Answer(_id=answer_id)
        return answer.delete_answer()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)


@answer_router.put("/update_answer/")
async def update_answer(model: AnswerPut) -> str:
    try:
        new_model = dict(model)
        new_model["_id"] = new_model.pop("id")
        answer = Answer(**dict(new_model))
        return answer.update_answer()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)
