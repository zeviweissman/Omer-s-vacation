from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Country

class CountryType(SQLAlchemyObjectType):
    class Meta:
        model = Country