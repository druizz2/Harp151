import requests
import json

base_url = f"https://api.weather.gov/points/"

"""
This method will return the address of the nearest forecast office to
Binghamton, NY. 
"""
def return_address(lat, lon):
    location = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json_location = location.json()
    office_url = json_location["properties"]["forecastOffice"]  
    # office_url prints a url to the nested dictionary, 
    # so need to do .get(officeurl) again
    get_office = requests.get(office_url)
    office_json = get_office.json()
    print(office_json["address"])


return_address(42.098701, -75.912537)
