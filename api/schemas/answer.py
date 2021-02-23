from pydantic import BaseModel, EmailStr, Field


class AbsAnswer(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    owner: EmailStr


class AnswerIn(AbsAnswer):
    announcement: int


class AnswerOut(AbsAnswer):
    created_time: str


class AnswerPut(BaseModel):
    id: int
    text: str = Field(..., min_length=4, max_length=128)
