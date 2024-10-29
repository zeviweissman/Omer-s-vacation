from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship


class Vacation(Base):
    __tablename__ = "vacation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    student_id = Column(Integer, ForeignKey('student.id'))

    student = relationship("Student", back_populates="vacations", lazy='joined')
    country = relationship("Country", back_populates="vacations", lazy='joined')