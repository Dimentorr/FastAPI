from models import Base, engine
from models import Task, Users, Tokens
from sqlalchemy.orm import sessionmaker

from security import security
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
        if not session.query(Task).filter(Task.name == name).first():
            new_task = Task(name=name, description=description, date_end=datetime.now()+timedelta(days=time_to_complete))
            session.add(new_task)
        else:
            return {'message': 'Task already exists', 'status': '400'}
    except Exception as e:
        end_sessions_on_exception(session)
        return {'message': 'Incorrect data', 'status': '400'}
    commit(session)


def create_user(name: str, password: str):
    """
    :param name: (str)
    :param password: (str)
    :return: None
    """
    session = create_new_session()
    try:
        if not session.query(Users).filter(Users.name == name).first():
            if hash_password := security.encode_data(password):
                new_user = Users(name=name, password=hash_password)
                session.add(new_user)
            else:
                return {'message': 'Server Error', 'status': '500'}
        else:
            return {'message': 'User already exists', 'status': '400'}
    except Exception as e:
        print(e)
        end_sessions_on_exception(session)
        return {'message': 'Incorrect data', 'status': '400'}
    commit(session)


def get_or_create_token(name: str, password: str):
    """
    :param name: username(str)
    :param password: password of the account(str)
    :return: api-token(str)
    """
    session = create_new_session()
    input_password = security.encode_data(password)

    if user := session.query(Users).filter_by(name=name, password=input_password).first():
        if token := session.query(Tokens).filter(Tokens.user == user.id).first():
            end_session(session)
            return {'status': '200', 'token': token.token}
        api_token = security.create_api_token()
        token = Tokens(token=api_token, user=user.id)
        session.add(token)
        commit(session)
        return {'status': '200', 'token': api_token}
    else:
        print(session.query(Users).join(Tokens, Users.id == Tokens.user).all())
        return {'message': 'User not find', 'status': '404'}


def check_token(token):
    session = create_new_session()
    if session.query(Tokens).filter(Tokens.token == token).first():
        end_session(session)
        return True
    end_session(session)
    return False


def get_all_tasks():
    session = create_new_session()
    tasks = session.query(Task).all()
    end_session(session)
    return tasks


def edit_task(data: dict):
    session = create_new_session()
    task = session.query(Task).filter_by(id=data['id']).first()
