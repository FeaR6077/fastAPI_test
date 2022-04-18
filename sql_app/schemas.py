from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    task_id: str
    user_id: str
    description: str
    completed: bool
