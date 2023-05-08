from fastapi import FastAPI

from api import router

app = FastAPI()
app.include_router(router)



'''''fsafasfas
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
'''