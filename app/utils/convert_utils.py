from app.models import Country, Student
from typing import Dict, List
import toolz as t


def dict_to_country_model(dict: Dict) -> Country:
    return Country(
    name=t.get_in(['name','common'], dict),
    region=t.get_in(['region'], dict),
    capital=t.get_in(['capital', 0], dict)
    )


def json_to_list_of_country_model(json) -> List[Country]:
    return [dict_to_country_model(country) for country in json]