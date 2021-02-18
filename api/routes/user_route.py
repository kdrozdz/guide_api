from typing import List

from fastapi import APIRouter, Body, HTTPException
from api.schemas.user import UserEmail, UserInformation

from api.models.user import User

user_router = APIRouter(tags=["User", ])


@user_router.post("/get_user/", response_model=UserInformation)
async def get_user(email: UserEmail) -> UserInformation:
    try:
        user = User(**dict(email))
        return user.get_user_all_info()
    except:
        raise HTTPException(status_code=400 , detail="Check your request data ")

@user_router.post("/get_all_user_order_by/", response_model=List[UserInformation])
async def get_user(order_by: str = Body(...) ) -> List[UserInformation]:
    try:
        user = User()
        return user.get_all_users_order_by(order_by)
    except:
        raise HTTPException(status_code=400 , detail="Check your request data ")
