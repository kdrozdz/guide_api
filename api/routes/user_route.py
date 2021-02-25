from typing import List

from pydantic import EmailStr

from fastapi import APIRouter, Body, HTTPException
from starlette import status

from api.const import MESSAGE_400
from api.schemas.user import UserInformation, UserAllInformation

from api.models.user import User

user_router = APIRouter(tags=["User", ])


@user_router.post("/get_user/", response_model=UserAllInformation)
async def get_user(email: EmailStr) -> UserAllInformation:
    try:
        user = User(email=email)
        return user.get_user_all_info()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)


@user_router.post("/get_all_user_order_by/", response_model=List[UserInformation])
async def get_user(order_by: str = Body(...)) -> List[UserInformation]:
    try:
        user = User()
        return user.get_all_users_order_by(order_by)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)
