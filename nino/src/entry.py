from fastapi import FastAPI, Request
from pydantic import BaseModel

async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Nino!"}

# @app.get("/env")
# async def root(req: Request):
#     env = req.scope["env"]
#     return {"message": "Here is an example of getting an environment variable: " + env.MESSAGE}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}










# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Welcome to": "Nino"}








# from fastapi import FastAPI
# import httpx

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/external-api")
# async def call_external_api():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://api.example.com/data")
#         return response.json()























































# from js import Response

# async def on_fetch(request, env):
#     return Response.new("Welcome to Nino")