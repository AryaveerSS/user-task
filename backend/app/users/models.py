from app.core.database import base
from sqlalchemy import Column,Integer,DateTime,Boolean,String
from sqlalchemy.orm import relationship
from datetime import datetime

class user_model(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    role = Column(String,default="user")
    tasks = relationship("Task",back_populates="owner",cascade="all, delete")