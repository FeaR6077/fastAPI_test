from pydoc import describe
from sqlalchemy.orm import Session

from . import models, schemas


def get_task(db: Session, task_id: str):
    return db.query(models.Task).filter(models.Task.task_id == task_id).first()


def get_task_by_user(db: Session, user_id: str):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()


def create_task(db: Session, task: schemas.TaskBase):
    db_task = models.Task(
        task_id=task.task_id,
        user_id=task.user_id,
        description=task.description,
        completed=False,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
