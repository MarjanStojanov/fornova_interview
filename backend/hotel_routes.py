from fastapi import APIRouter, Depends

from auth import get_api_key
from hotel_service import HotelService
from models import SearchSchema


hotel_router = APIRouter()


@hotel_router.get("/browse")
def browse_hotels(api_key: str = Depends(get_api_key), page: int = 1, limit: int = 10):
    results = HotelService().browse(page=page, limit=limit)
    return {"hotels": results}


@hotel_router.post("/search")
def search_hotels(payload: SearchSchema, api_key: str = Depends(get_api_key)):
    results = HotelService().search(
        keyword=payload.keyword, page=payload.page, limit=payload.limit
    )
    return {"hotels": results}
