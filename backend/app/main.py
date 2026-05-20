from fastapi import FastAPI
from app.tasks.models import Task
# from app.tasks.controller import router as task_router
from app.core.database import base
from app.core.database import engine

from app.users.models import user_model
from fastapi.middleware.cors import CORSMiddleware
from app.users.routes import router as user_router
from app.tasks.routes import router as task_router
from app.admin.router import router as admin_router
from app.middleware.error_handler import register_exception_handlers

base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task Management API",
    description="""
    Scalable FastAPI backend with:

    - JWT Authentication
    - Role-Based Access Control
    - Protected CRUD APIs
    - PostgreSQL Integration
    - Modular Architecture
    """,
    version="1.0.0"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)
register_exception_handlers(app)
app.include_router(
    admin_router,
    prefix="/api/v1"
)
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