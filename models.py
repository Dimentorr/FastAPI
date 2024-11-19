from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tasks.db', echo=True)
Base = declarative_base()


class Task(Base):
    __tablename__ = 'Задачи'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, name='Название')
    description = Column(String, name='Описание')
    date_end = Column(Date, name='Дата окончания')

    def __repr__(self):
        return f"<Task(name='{self.name}', date_end='{self.date_end}')>"
