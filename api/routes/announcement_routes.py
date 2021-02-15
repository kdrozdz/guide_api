from typing import List

from fastapi import APIRouter, Body

from api.schemas.announcement import AnnouncementIn, AnnouncementOut

from api.models.announcement import Announcement


announcement_router = APIRouter(tags=["Announcement", ])


@announcement_router.post("/create_announcement/",)
async def create_announcement(model: AnnouncementIn) -> str:
    announcement = Announcement(**dict(model))
    return announcement.save()

@announcement_router.post("/get_announcement/", response_model=AnnouncementOut)
async def get_announcement(id: str = Body(...)) -> List[AnnouncementOut]:
    announcement = Announcement(_id=id)
    return announcement.get_specific_announcement()
