import os

import uvicorn
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

from api.routes.advertisement_routes import advertisement_router
from api.routes.user_routes import user_router
from api.routes.token_routes import token_router
from database.migration import run_create_tables


load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if os.environ["DATABASE_CREATE_TABLE"]:
    run_create_tables()

app = FastAPI()
app.include_router(advertisement_router)
app.include_router(user_router)
app.include_router(token_router)

@app.get("/")
async def welocme() -> str:
    return "welocme"


if __name__ == "__main__":
    uvicorn.run("core:app", host="localhost", port=8001, reload=True, debug=True, workers=2)
