from app.gql.types import CountryType, StudentType
from graphene import ObjectType, List
import app.repository.student_repository as student_repos
import app.repository.country_repository as country_repos


class Query(ObjectType):
    students = List(StudentType)
    countries = List(CountryType)


    @staticmethod
    def resolve_students(root, info):
        return student_repos.get_all_students().value_or(None)

    @staticmethod
    def resolve_countries(root, info):
        return country_repos.get_all_countries().value_or(None)