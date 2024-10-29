from typing import List
from app.database.psql import get_session
from app.models import Country
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError


def get_all_countries() -> Result[List[Country], str]:
    with get_session() as session:
        try:
            return Success(session.query(Country).all())
        except SQLAlchemyError as e:
            return Failure(str(e))