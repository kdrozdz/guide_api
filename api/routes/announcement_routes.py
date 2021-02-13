from fastapi import APIRouter, Depends
from api.authorization import oauth2_scheme

from api.schemas.announcement import AnnouncementIn

from api.models.announcement import Announcement


announcement_router = APIRouter(dependencies=(Depends(oauth2_scheme), ), tags=["Announcement", ])


@announcement_router.post("/create_announcement/",)
async def create_announcement(model: AnnouncementIn) -> str:
    announcement = Announcement(**dict(model))
    return announcement.save()
