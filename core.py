import uvicorn
from fastapi import FastAPI


from api.routes.announcement_routes import announcement_router
from api.routes.answer_router import answer_router
from api.routes.user_route import user_router
from api.routes.reputation_routes import reputation_router
from api.routes.token_register_router import token_register_router


app = FastAPI()
app.include_router(announcement_router)
app.include_router(answer_router)
app.include_router(user_router)
app.include_router(reputation_router)
app.include_router(token_register_router)


@app.get("/",)
async def welcome() -> {}:
    return f"Hello, put /docs to your url path it should looks like http://localhost:8000/docs "


if __name__ == "__main__":
    uvicorn.run("core:app", host="localhost", port=8000, reload=True, debug=True, workers=2)
