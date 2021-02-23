import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from ..schemas.token import Token

from ..schemas.user import UserIn

from ..models.user import User


token_register_router = APIRouter(tags=["Auth-Reg", ])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ['SECRET_KEY'], algorithm=os.environ['ALGORITHM'])
    return encoded_jwt


@token_register_router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User(email=form_data.username, password=form_data.password)
    if user.authenticate():
        access_token_expires = timedelta(minutes=int(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']))

        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@token_register_router.post("/registre_users/")
async def user_create(model: UserIn) -> str:
    """
    put location like e.g 3 in str
    ("1", "Białystok"),
    ("2", "Bydgoszcz"),
    ("3", "Gdańsk"),
    ("4", "Gorzów Wielkopolski"),
    ("5", "Katowice"),
    ("6", "Kielce"),
    ("7", "Kraków"),
    ("8", "Lublin"),
    ("9", "Łódź"),
    ("10", "Olsztyn"),
    ("11", "Opole"),
    ("12", "Poznań"),
    ("13", "Rzeszów"),
    ("14", "Szczecin"),
    ("15", "Toruń"),
    ("16", "Warszawa"),
    ("17", "Wrocław"),
    ("18", "Zielona Góra")
    """
    user = User(**dict(model))
    return user.save()
