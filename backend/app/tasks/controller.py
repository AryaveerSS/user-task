from app.tasks.dtos import task_schema,task_schema_update
from sqlalchemy.orm import session
from app.tasks.models import task_model
from fastapi.responses import JSONResponse
from fastapi import HTTPException

def create_task(task:task_schema,db:session):
    new_task=task_model(

        id=task.id,
        task_name=task.task_name,
        description=task.description,
        is_completed=task.is_completed

    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return JSONResponse(status_code=200,content="task successfuly created")

def get_task(idd:int,db:session):
    # task = db.query(task_model).get(idd)
    task=  db.query(task_model).filter(task_model.id==idd).first()
    if task is None:
        raise HTTPException(status_code=404,detail=" task id is not in the database ")
    
    return {"status":"task fetched successfuly","data":task}

def getall_task(db:session):
    task=db.query(task_model).all()
    return task

def update_task(idd:int,task:task_schema_update,db:session):
    one_task=db.query(task_model).get(idd)
    if one_task is None:
        raise HTTPException(status_code=404,detail=" task id is not in the database ")
    
    task_dict=task.model_dump(exclude_unset=True)
    for col,value in task_dict.items():
        setattr(one_task,col,value)

    db.add(one_task)

    db.commit()

    db.refresh(one_task)

    return {"status":"task updated successfuly","data":one_task}
