from sqlalchemy import Column, Integer, String
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship


class Country(Base):
   __tablename__ = "country"
   id = Column(Integer, primary_key=True, autoincrement=True)
   region = Column(String)
   capital = Column(String)
   name = Column(String)

   vacations = relationship("Vacation", back_populates="country")

