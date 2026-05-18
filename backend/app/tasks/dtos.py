from pydantic import BaseModel,field_validator
from pydantic import Field

from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


    @field_validator("title")
    @classmethod
    def validate_title(cls, value):

        if len(value) < 3:
            raise ValueError(
                "Task title should have at least 3 characters"
            )

        if len(value) > 100:
            raise ValueError(
                "Task title cannot exceed 100 characters"
            )

        return value

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


    @field_validator("title")
    @classmethod
    def validate_title(cls, value):

        if value is not None:

            if len(value) < 3:
                raise ValueError(
                    "Task title should have at least 3 characters"
                )

            if len(value) > 100:
                raise ValueError(
                    "Task title cannot exceed 100 characters"
                )

        return value

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True