from pydantic import BaseModel, EmailStr, Field


class ReputationOut(BaseModel):
    rating: int = Field(..., gt=0, le=10)
    text: str = Field(None, max_length=64)
    from_user: EmailStr


class ReputationIn(ReputationOut):
    to_user: EmailStr
