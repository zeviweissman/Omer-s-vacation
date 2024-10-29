from app.gql.mutations import AddVacation
from graphene import ObjectType

class Mutation(ObjectType):
    AddVacation = AddVacation.Field()
