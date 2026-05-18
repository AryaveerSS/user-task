from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import status
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.tasks.dtos import TaskCreate
from app.tasks.dtos import TaskUpdate
from app.tasks.dtos import TaskResponse

from app.tasks.controller import create_task_controller
from app.tasks.controller import get_tasks_controller
from app.tasks.controller import get_single_task_controller
from app.tasks.controller import update_task_controller
from app.tasks.controller import delete_task_controller

from app.users.dependencies import get_current_user

from app.users.models import user_model

router = APIRouter()


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: user_model = Depends(get_current_user)
):
    return create_task_controller(
        task_data,
        db,
        current_user
    )


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    skip: int = 0,
    limit: int = Query(default=10, le=100),
    search: str | None = None,
    completed: bool | None = None,
    db: Session = Depends(get_db),
    current_user: user_model = Depends(get_current_user)
):
    return get_tasks_controller(
        db,
        current_user,
        skip,
        limit,
        search,
        completed
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_single_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: user_model = Depends(get_current_user)
):
    return get_single_task_controller(
        task_id,
        db,
        current_user
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: user_model = Depends(get_current_user)
):
    return update_task_controller(
        task_id,
        task_data,
        db,
        current_user
    )


@router.delete(
    "/{task_id}"
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: user_model = Depends(get_current_user)
):
    return delete_task_controller(
        task_id,
        db,
        current_user
    )


@router.get("/admin")
def admin_route(
    current_user = Depends(
        get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return {
        "message": "Welcome admin"
    }