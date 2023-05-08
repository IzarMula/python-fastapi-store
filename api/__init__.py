from fastapi import APIRouter

from api.items import items_router
from api.items.v1 import ItemsController

router = APIRouter()
router.include_router(items_router, prefix="/items", tags=["Items"])

__all__ = ["router"]

