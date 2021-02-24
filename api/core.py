import os

import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv

from api.routes.announcement_routes import announcement_router
from api.routes.answer_router import answer_router
from api.routes.user_route import user_router
from api.routes.reputation_routes import reputation_router
from api.routes.token_register_router import token_register_router
from api.database.populate import create_users
from database.migration import run_create_tables


load_dotenv()

if os.environ["DATABASE_CREATE_TABLE"]:
    run_create_tables()

if os.environ["DATABASE_POPULATE"]:
    create_users()

app = FastAPI()
app.include_router(announcement_router)
app.include_router(answer_router)
app.include_router(user_router)
app.include_router(reputation_router)
app.include_router(token_register_router)


if __name__ == "__main__":
    uvicorn.run("core:app", host="localhost", port=8002, reload=True, debug=True, workers=2)
