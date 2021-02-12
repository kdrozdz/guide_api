from fastapi import APIRouter
from api.schemas.user import UserEmail, UserInformation

from api.models.user import User

user_router = APIRouter(tags=["User", ])


@user_router.post("/get_user/")
async def get_user(email: UserEmail) -> UserInformation:
    user = User(**dict(email))
    return user.get_user_all_info()
