from sqlalchemy import Column, Integer, String
from app.settings.psql_config import Base

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Age = Column(Integer)
    Favorite_Language = Column(String)
    Favorite_Framework = Column(String)
