from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import base

class task_model(base):
    __tablename__="tasks"

    id=Column(Integer,primary_key=True)
    task_name=Column(String)
    description=Column(String)
    is_completed=Column(Boolean,default=False)