from graphene import InputObjectType, Date, Int

class VactionInput(InputObjectType):
    start_date = Date()
    student_id = Int()
    country_id = Int()