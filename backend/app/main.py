from fastapi import FastAPI
from app.core.database import base,engine
from app.task.models import task_model
from app.task.routes import task_router
from app.user.routes import user_router
base.metadata.create_all(engine)

app=FastAPI(title=" task management app ")

app.include_router(task_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {
        "message": "Task Management API Running"
    }