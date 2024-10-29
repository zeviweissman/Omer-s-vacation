from app.gql.types import CountryType, StudentType
from graphene import ObjectType, List


class Query(ObjectType):
    students = List(StudentType)
    countries = List(CountryType)