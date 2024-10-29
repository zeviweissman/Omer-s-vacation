import datetime
from app.gql.types import VacationType
from app.models import Vacation
import app.repository.vacation_repository as vacation_repos
from graphene import String, Mutation, Field
from app.gql.inputs import VactionInput




class AddVacation(Mutation):
   class Arguments():
      vacation_input = VactionInput()
   vacation = Field(VacationType)

   @staticmethod
   def mutate(root, info, vacation_input: VactionInput):
      vacation_to_add = Vacation(
         start_date=vacation_input.start_date,
         end_date=datetime.datetime.now(),
         student_id=vacation_input.student_id,
         country_id=vacation_input.country_id)

      vacation = vacation_repos.insert_vacation(vacation_to_add).value_or(None)
      return AddVacation(vacation=vacation) if vacation else AddVacation(vacation=None)