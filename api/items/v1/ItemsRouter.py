from fastapi import APIRouter, Query, Depends
from starlette.status import HTTP_200_OK

from .ItemsController import ItemsController

items_router = APIRouter()

@items_router.get("",
                  description="call the loli",
                  status_code=HTTP_200_OK)
async def get_item_by_id(itemId: int = Query(), itemController: ItemsController = Depends()):
    return await itemController.read_item(item_id=itemId)