from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/task/")
def create_task(task: schemas.TaskBase, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task.task_id)
    print("done")
    if db_task:
        raise HTTPException(status_code=400, detail="task_id already taken")
    crud.create_task(db=db, task=task)
    return {"status": 201, "message": "task created"}


@app.get("/tasks/")
def get_tasks(user_id: str, db: Session = Depends(get_db)):
    tasks = crud.get_task_by_user(db, user_id=user_id)
    return tasks
