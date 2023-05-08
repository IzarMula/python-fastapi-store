class ItemsController:
    def __init__(self):
        pass

    async def read_item(self, item_id: int):
        return {"item_id": item_id}