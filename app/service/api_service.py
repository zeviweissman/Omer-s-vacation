import requests
import app.utils.convert_utils as u

URL = "https://restcountries.com/v3.1/all"



def get_from_api():
    response = requests.request('GET', URL)
    json  = response.json()
    return u.json_to_list_of_country_model(json)

