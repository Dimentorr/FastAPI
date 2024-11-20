from fastapi import FastAPI
from models import Base, engine
from sql_operations import add_task, get_all_tasks
from validate import Task as ValidateTask

from security import security

app = FastAPI()
Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/api/token")
def get_token():
    return security.create_access_token()


@app.get("/v1/api/tasks")
def get_tasks_api():
    return get_all_tasks()


@app.post("/v1/api/add_task")
def add_task_api(new_task: ValidateTask):
    if error := add_task(name=new_task.name, description=new_task.description,
                         time_to_complete=new_task.time_to_complete):
        return error
    return {'message': 'Task added successfully', 'status': 200}
