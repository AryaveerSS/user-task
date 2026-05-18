from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.users.models import user_model

from app.users.routes import router as user_router
from app.tasks.routes import router as task_router

from app.middleware.error_handler import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(
    user_router,
    prefix="/api/v1/users",
    tags=["Users"]
)

app.include_router(
    task_router,
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)


@app.get("/")
async def root():
    return {
        "message": "API Running"
    }