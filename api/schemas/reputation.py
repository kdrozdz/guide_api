from pydantic import BaseModel, Field


class ReputationIn(BaseModel):
    rating: int = Field(..., gt=0, le=10)
    text: str = Field(None, max_length=64)
    from_user: int
    to_user: int
