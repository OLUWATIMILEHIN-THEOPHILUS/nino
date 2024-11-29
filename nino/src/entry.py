from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Welcome to": "Nino"}



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