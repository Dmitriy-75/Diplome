from app.backend.db import Base
from sqlalchemy import Column,  Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    age = Column(Integer)
    job = Column(String)
    tasks = relationship('Task', back_populates="user")

    def __str__(self):
        return f'{self.firstname} {self.lastname}'



# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))



