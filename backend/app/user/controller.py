from sqlalchemy.orm import Session
from app.user.models import user_model
from app.user.dtos import user_schema
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def register(user:user_schema,db:Session):
    #username validation
    if db.query(user_model).filter(user_model.username==user.username).first():
        raise HTTPException(status_code=409,detail="username is taken")
    
    # email validation
    if db.query(user_model).filter(user_model.email==user.email).first():
        raise HTTPException(status_code=409,detail="a user with this email already exists")
    
    new_user=user_model(
        username=user.username,
        email=user.email,
        hash_password=user.password

    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)                      
    return {"message":"user registered successfully"}