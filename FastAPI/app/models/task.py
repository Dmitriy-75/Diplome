from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *



class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    slug = Column(String, index=True)
    user = relationship('User', back_populates="tasks")

    def __str__(self):
        return f'{self.title}'


# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))


