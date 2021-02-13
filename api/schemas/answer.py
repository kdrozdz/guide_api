from pydantic import BaseModel, Field


class AnswerIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    owner: int
    announcement: int