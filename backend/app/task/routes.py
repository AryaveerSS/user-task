from fastapi import APIRouter,Depends
from src.task.controller import create_task,get_task,getall_task,update_task
from sqlalchemy.orm import session 
from src.task.dtos import task_schema,task_schema_update
from src.utils.db import get_db

task_router=APIRouter(prefix="/tasks")

@task_router.post("/create")
def create_task_endpoint(task:task_schema,db=Depends(get_db)):
    return create_task(task,db)

@task_router.get("/view/{id}")
def get_task_endpoint(id:int,db=Depends(get_db)):
    return get_task(id,db)

@task_router.get("/view")
def getall_task_endpoint(db:session=Depends(get_db)):
    return getall_task(db)

@task_router.put("/update_task/{id}")
def update_task_endpoint(id:int,task:task_schema_update,db:session=Depends(get_db)):
    return update_task(id,task,db)