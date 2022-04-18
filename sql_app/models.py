from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Task(Base):
    __tablename__ = "task"

    task_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, unique=False)
    description = Column(String, unique=False)
    completed = Column(Boolean, default=False)
