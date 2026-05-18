from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.users.dependencies import (
    admin_required
)

from app.users.models import user_model

from app.tasks.models import Task


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(
        admin_required
    )
):

    users = db.query(user_model).all()

    return users


@router.get("/tasks")
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(
        admin_required
    )
):

    tasks = db.query(Task).all()

    return tasks


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
        admin_required
    )
):

    user = db.query(user_model).filter(
        user_model.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted"
    }


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
        admin_required
    )
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)

    db.commit()

    return {
        "message": "Task deleted"
    }