import os

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv

from database.migration import run_create_tables
from api.routes.user_routes import user_router
from api.schemas.token import Token
from api.models.user import User

load_dotenv()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if os.environ["DATABASE_CREATE_TABLE"]:
    run_create_tables()

app = FastAPI()
app.include_router(user_router)

@app.get("/")
async def welocme() -> str:
    return "welocme"


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User(email = form_data.username, password = form_data.password)
    return user.authenticate()
    # user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Incorrect username or password",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     data={"sub": user.username}, expires_delta=access_token_expires
    # )
    # return {"access_token": access_token, "token_type": "bearer"}

if __name__ == "__main__":
    uvicorn.run("core:app", host="localhost", port=8001, reload=True, debug=True, workers=2)
