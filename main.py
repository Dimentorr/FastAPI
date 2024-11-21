from fastapi import FastAPI

from models import Base, engine
from sql_operations import add_task, get_all_tasks, create_user, get_or_create_token
from validate import Task as ValidateTask, Users as ValidateUsers

from security import security


api_app = FastAPI()
Base.metadata.create_all(engine)


@api_app.get("/")
def read_root():
    return {"Hello": "World"}


@api_app.post("/v1/api/create_user")
def new_user(user: ValidateUsers):
    if error := create_user(name=user.name, password=user.password):
        return error
    return {'message': 'User added successfully', 'status': 200}


@api_app.get("/v1/api/token")
def get_token(user: ValidateUsers):
    return get_or_create_token(name=user.name, password=user.password)


@api_app.get("/v1/api/tasks")
def get_tasks_api():
    return get_all_tasks()


@api_app.post("/v1/api/add_task")
def add_task_api(new_task: ValidateTask):
    if error := add_task(name=new_task.name, description=new_task.description,
                         time_to_complete=new_task.time_to_complete):
        return error
    return {'message': 'Task added successfully', 'status': 200}
