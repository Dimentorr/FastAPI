from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
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
    status = Column(Integer, ForeignKey('Статусы.name'), default='В процессе')

    def __str__(self):
        return f"name={self.name}, status={self.status}"


class StatusTask(Base):
    __tablename__ = 'Статусы'

    name = Column(String, nullable=False, primary_key=True)

    def __str__(self):
        return f"{self.name}"
