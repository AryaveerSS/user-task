from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session
from app.utils.logger import logger 
from app.tasks.models import Task
from app.tasks.dtos import TaskCreate
from app.tasks.dtos import TaskUpdate

from app.users.models import user_model


def create_task_controller(
    task_data: TaskCreate,
    db: Session,
    current_user: user_model
):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        owner_id=current_user.id
    )

    db.add(task)
    db.commit()
    logger.info(
    f"Task created: "
    f"{task.title}"
    )
    db.refresh(task)

    return task


def get_tasks_controller(
    db: Session,
    current_user: user_model,
    skip: int,
    limit: int,
    search: str | None,
    completed: bool | None
):
    query = db.query(Task).filter(
        Task.owner_id == current_user.id
    )

    if search:
        query = query.filter(
            Task.title.ilike(f"%{search}%")
        )

    if completed is not None:
        query = query.filter(
            Task.completed == completed
        )

    tasks = query.offset(skip).limit(limit).all()

    return tasks


def get_single_task_controller(
    task_id: int,
    db: Session,
    current_user: user_model
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if (
        task.owner_id != current_user.id
        and current_user.role != "admin"
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    return task


def update_task_controller(
    task_id: int,
    task_data: TaskUpdate,
    db: Session,
    current_user: user_model
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own tasks"
        )

    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task_controller(
    task_id: int,
    db: Session,
    current_user: user_model
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if (
        task.owner_id != current_user.id
        and current_user.role != "admin"
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )   
    logger.info(
    f"Task deleted: "
    f"{task.title}"
        )
    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }