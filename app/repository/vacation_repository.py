from app.database.psql import get_session
from returns.result import Success, Failure, Result
from app.models import Vacation
from sqlalchemy.exc import SQLAlchemyError


def insert_vacation(vacation: Vacation) -> Result[Vacation, str]:
    with get_session() as session:
        try:
            session.add(vacation)
            session.commit()
            session.refresh(vacation)
            return Success(vacation)
        except SQLAlchemyError as e:
            return Failure(str(e))
