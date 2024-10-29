from typing import List
from app.database.psql import get_session
from app.models import Student, Vacation, Country
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError


def get_all_students() -> Result[List[Student], str]:
    with get_session() as session:
        try:
            return Success(session.query(Student).all())
        except SQLAlchemyError as e:
            return Failure(str(e))


def get_all_students_by_country(country_name: str):
    with get_session() as session:
        try:
            return Success(
                session.query(Student)
                .join(Vacation)
                .join(Country)
                .filter(Country.name == country_name)
                .all()
            )
        except SQLAlchemyError as e:
            return Failure(str(e))