import os

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from database.migration import run_create_tables
from schemas.user import UserIn

from models.user import User
load_dotenv()

if os.environ["DATABASE_CREATE_TABLE"]:
    run_create_tables()

app = FastAPI()


@app.get("/")
async def welocme() -> dict:
    return {
        "welocme": "welcome"
    }


@app.post("/create_users/")
async def user_create(model: UserIn) -> dict:
    user = User(**dict(model))

    try:
        user.save()

    except:
        return {
            "test": "123"
        }


if __name__ == "__main__":
    uvicorn.run("core:app", host="localhost", port=8001, reload=True, debug=True, workers=2)
