from enum import Enum

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Task(BaseModel):
    task_id: str
    user_id: str
    description: str
    completed: bool
