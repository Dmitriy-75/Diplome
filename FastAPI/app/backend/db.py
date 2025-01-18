from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# engine = create_engine('sqlite:///C://Users//kolya//PycharmProjects//Fastap//app//taskmanager.db', echo=True)
engine = create_engine('sqlite:///./taskmanager.db', echo=True)
SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass

