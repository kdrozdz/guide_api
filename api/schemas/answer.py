from pydantic import BaseModel, Field


class AbsAnswer(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    owner: str

class AnswerIn(AbsAnswer):
    announcement: int

class AnswerOut(AbsAnswer):
    created_time: str

class AnswerPut(BaseModel):
    id: str
    text: str = Field(..., min_length=4, max_length=128)