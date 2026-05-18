from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import base


class Task(base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,index=True)

    title = Column(String,nullable=False)

    description = Column(String,nullable=True)

    completed = Column(Boolean,default=False)

    created_at = Column(DateTime,default=datetime.utcnow)

    owner_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("user_model",back_populates="tasks")