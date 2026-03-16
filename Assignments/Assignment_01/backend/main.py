from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from . import models, database

# Create tables in DB (if they don't exist)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Task Management API")

# Pydantic models for validation
class TaskBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
