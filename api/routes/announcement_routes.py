from typing import List

from fastapi import APIRouter, Body, HTTPException
from starlette import status

from ..schemas.announcement import AnnouncementIn, AnnouncementOut, LocationOrOwner, ValueLocationOrOwner, \
    AnnouncementListOut, AnnouncementUpdateIn, LanguageLocation
from ..models.announcement import Announcement
from ..const import MESSAGE_400

announcement_router = APIRouter(tags=["Announcement", ])


@announcement_router.post("/create_announcement/",)
async def create_announcement(model: AnnouncementIn) -> str:
    """
    location: e.g "2"  (check register user route for a info about location)

    owner: e.g "user@example.com"
    """
    try:
        announcement = Announcement(**dict(model))
        return announcement.save()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)


@announcement_router.get("/get_announcement/", response_model=AnnouncementOut)
async def get_announcement(id: int) -> List[AnnouncementOut]:
    try:
        announcement = Announcement(_id=id)
        return announcement.get_specific_announcement()
    except:
        raise HTTPException(status_code=400, detail=MESSAGE_400)


@announcement_router.post("/get_list_of_announcement/",
                          response_model=List[AnnouncementListOut])
async def get_list_of_announcement(location_or_owner: LocationOrOwner, value: ValueLocationOrOwner) -> List[AnnouncementOut]:
    """
       It give you back a list of announcements assign for specific user or concrete city.

       Put value for owner like email e.g "user@example.com"

       Put value for location like str e.g "5" check register user
       """
    announcement = Announcement()
    return announcement.get_list_of_announcement_location_or_owner(value.value, location_or_owner.value)


@announcement_router.delete("/delete_announcement/",)
async def delete_announcement(id: int) -> str:
    try:
        announcement = Announcement(_id=id)
        return announcement.delete_announcement()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)

@announcement_router.put("/update_announcement/",)
async def delete_announcement(model: AnnouncementUpdateIn) -> any:
    """
    location: like str check register user

    owner: e.g "user@example.com
    """
    try:
        new_model = dict(model)
        new_model["_id"] = new_model.pop("id")
        announcement = Announcement(**dict(new_model))
        return announcement.announcement_update_row()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)

@announcement_router.post("/search_announcement_by_language_location/", response_model=List[AnnouncementListOut])
async def search_announcement_by_language_location(languageLocation: LanguageLocation) -> List[AnnouncementOut]:
    """
    location: eg "5" or leave empty ""(without whitespaces)(check register user route for a info about location)
    language" eg "english"

    You can use both of them in this same time for a better results
    """
    try:
        announcement = Announcement(language=languageLocation.language, location=languageLocation.location)
        return announcement.search_announcement_by_language_location()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MESSAGE_400)
