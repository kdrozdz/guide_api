from pydantic import BaseModel, Field


class AnswerIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    owner: str
    announcement: int

class AnswerOut(BaseModel):
    text: str
    owner: str
    created_time: str