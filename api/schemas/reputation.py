from pydantic import BaseModel, Field


class ReputationOut(BaseModel):
    rating: int = Field(..., gt=0, le=10)
    text: str = Field(None, max_length=64)
    from_user: int


class ReputationIn(ReputationOut):
    to_user: int
