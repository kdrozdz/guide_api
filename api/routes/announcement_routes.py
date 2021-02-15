from typing import List, Union

from fastapi import APIRouter, Body

from api.schemas.announcement import AnnouncementIn, AnnouncementOut, LocationOrOwner, ValueLocationOrOwner, \
    AnnouncementListOut

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


@announcement_router.post("/get_list_of_announcement/", response_model= Union[AnnouncementListOut, List[AnnouncementListOut]])
async def get_announcement(location_or_owner: LocationOrOwner, value: ValueLocationOrOwner) -> List[AnnouncementOut]:

    announcement = Announcement()
    return announcement.get_list_of_announcement_location_or_owner(value.value, location_or_owner.value)