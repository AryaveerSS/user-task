from src.utils.db import base
from sqlalchemy import Column,Integer,DateTime,Boolean,String

class user_model(base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False)
    email=Column(String)
    hash_password=Column(String,nullable=False)