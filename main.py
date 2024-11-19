from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models import Base, engine
from sql_operations import add_task, get_all_tasks
from validate import Task as ValidateTask

app = FastAPI()
Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_all_tasks")
def get_tasks_api():
    return get_all_tasks()


@app.post("/add_task")
def add_task_api(new_task: ValidateTask):
    print(new_task)
    add_task(name=new_task.name, description=new_task.description, time_to_complete=new_task.time_to_complete)
    return {"message": "Task added successfully"}
