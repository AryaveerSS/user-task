from pydantic import BaseModel, Field,Field
from typing import Annotated,Optional

class task_schema(BaseModel):

    id:Annotated[int,Field(description="enter the task id" )]
    task_name:Annotated[str,Field(description="enter the task name")]
    description:Annotated[str,Field(description="enter the description of task")]
    is_completed:Annotated[bool,Field(default=False)]

class task_schema_update(BaseModel):
    task_name:Annotated[Optional[str],Field(description="enter the task name",example="study",default=None)]
    description:Annotated[Optional[str],Field(description="enter the description of task",default=None)]
    is_completed:Annotated[Optional[bool],Field(default=None)]