from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from src.user.models import user_model
from src.user.dtos import user_schema
from src.utils.db import get_db
from src.user.controller import register

user_router=APIRouter(prefix="/user")


@user_router.post("/register")
def reg(user:user_schema,db:Session=Depends(get_db)):
    return register(user,db)