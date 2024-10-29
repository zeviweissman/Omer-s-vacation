from typing import List
from app.database.psql import get_session
from app.models import Student
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError


def get_all_students() -> Result[List[Student], str]:
    with get_session() as session:
        try:
            return Success(session.query(Student).all())
        except SQLAlchemyError as e:
            return Failure(str(e))