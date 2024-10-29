from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Student


class StudentType(SQLAlchemyObjectType):
    class Meta:
        model = Student