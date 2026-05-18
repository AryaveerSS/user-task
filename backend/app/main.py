from fastapi import FastAPI
from src.utils.db import base,engine
from src.task.models import task_model
from src.task.routes import task_router
from src.user.routes import user_router
base.metadata.create_all(engine)

app=FastAPI(title=" task management app ")
app.include_router(task_router)
app.include_router(user_router)