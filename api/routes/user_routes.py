from fastapi import APIRouter
from api.schemas.user import UserIn

from api.models.user import User

user_router = APIRouter()


@user_router.post("/registre_users/")
async def user_create(model: UserIn) -> str:
    user = User(**dict(model))
    return user.save()
