from typing import List, Union

from fastapi import APIRouter, Body, HTTPException

from ..schemas.announcement import AnnouncementIn, AnnouncementOut, LocationOrOwner, ValueLocationOrOwner, \
    AnnouncementListOut
from ..models.announcement import Announcement
from ..const import MESSAGE_400

announcement_router = APIRouter(tags=["Announcement", ])


@announcement_router.post("/create_announcement/",)
async def create_announcement(model: AnnouncementIn) -> str:
    try:
        announcement = Announcement(**dict(model))
        return announcement.save()
    except:
        raise HTTPException(status_code=400 , detail=MESSAGE_400)


@announcement_router.get("/get_announcement/", response_model=AnnouncementOut)
async def get_announcement(id: str) -> List[AnnouncementOut]:
    try:
        announcement = Announcement(_id=id)
        return announcement.get_specific_announcement()
    except:
        raise HTTPException(status_code=400, detail=MESSAGE_400)


@announcement_router.post("/get_list_of_announcement/", response_model= Union[AnnouncementListOut, List[AnnouncementListOut]])
async def get_announcement(location_or_owner: LocationOrOwner, value: ValueLocationOrOwner) -> List[AnnouncementOut]:
    try:
        announcement = Announcement()
        return announcement.get_list_of_announcement_location_or_owner(value.value, location_or_owner.value)
    except:
        raise HTTPException(status_code=400, detail=MESSAGE_400)

