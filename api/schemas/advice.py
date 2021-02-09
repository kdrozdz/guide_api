from pydantic import BaseModel, Field


class AdviceIn(BaseModel):
    text: str = Field(..., min_length=4, max_length=128)
    owner: int
    advertisement: int