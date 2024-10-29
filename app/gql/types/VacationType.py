from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Vacation


class VacationType(SQLAlchemyObjectType):
    class Meta:
        model = Vacation