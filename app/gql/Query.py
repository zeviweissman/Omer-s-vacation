from app.gql.types import CountryType, StudentType
from graphene import ObjectType, List, String
import app.repository.student_repository as student_repos
import app.repository.country_repository as country_repos


class Query(ObjectType):
    students = List(StudentType)
    countries = List(CountryType)
    student_by_country = List(StudentType, country=String())


    @staticmethod
    def resolve_student_by_country(root, info, country):
        return student_repos.get_all_students_by_country(country).value_or(None)

    @staticmethod
    def resolve_students(root, info):
        return student_repos.get_all_students().value_or(None)

    @staticmethod
    def resolve_countries(root, info):
        return country_repos.get_all_countries().value_or(None)