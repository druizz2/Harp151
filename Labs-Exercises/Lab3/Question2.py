import requests 
import json 


base_url = "https://date.nager.at/api/v3/"

# Country
# Get Country info
country_code = 46
country_url = "https://date.nager.at/api/v3/CountryInfo/{country_code}"
get_country_info = (requests.get(country_url)).json()
