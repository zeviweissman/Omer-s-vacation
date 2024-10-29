import csv
from app.models import Student


FILEPATH = 'C:\\Users\\1\\PycharmProjects\\Omers_vacation\\assests\\students.csv'
def read_from_csv():
    with open(FILEPATH, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Student(**row) for row in reader]
