from app.database.psql import get_session
from app.service.api_service import get_from_api
from app.service.csv_service import read_from_csv


def init_data():
    countries = get_from_api()
    students = read_from_csv()
    with get_session() as session:
        session.add_all(countries)
        session.add_all(students)
        session.commit()