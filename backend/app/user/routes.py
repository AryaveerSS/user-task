from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.user.models import user_model
from app.user.dtos import user_schema
from app.core.database import get_db
from app.user.controller import register

user_router=APIRouter(prefix="/user")


@user_router.post("/register")
def reg(user:user_schema,db:Session=Depends(get_db)):
    return register(user,db)