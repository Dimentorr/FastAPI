from models import Base, engine
from models import Task
from sqlalchemy.orm import sessionmaker

from datetime import datetime, timedelta


def create_new_session():
    return sessionmaker(bind=engine)()


def commit(session):
    session.commit()
    session.close()


def end_session(session):
    session.close()


def end_sessions_on_exception(session):
    session.rollback()
    end_session(session)


def add_task(name: str, description: str, time_to_complete=7):
    """
    :param name: (str) name of the task
    :param description: (str) description of the task
    :param time_to_complete: (int) days
    :return: None
    """
    session = create_new_session()
    try:
        new_task = Task(name=name, description=description, date_end=datetime.now()+timedelta(days=time_to_complete))
        session.add(new_task)
    except Exception as e:
        end_sessions_on_exception(session)
        raise e
    commit(session)


def get_all_tasks():
    session = create_new_session()
    tasks = session.query(Task).all()
    end_session(session)
    return tasks

