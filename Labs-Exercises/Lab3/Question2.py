import requests
import json  # noqa: F401

base_url = "https://date.nager.at/api/v3/"

# Country

# Get Country info -> Returns country specific info based on country code
country_code = "AU"
country_url = f"https://date.nager.at/api/v3/CountryInfo/{country_code}"
get_country_info = (requests.get(country_url))
json_file = get_country_info.json()
print(json_file)

# Available Countries -> Returns all countries in API
available_countries_url = "https://date.nager.at/api/v3/AvailableCountries"
get_available_countries = requests.get(available_countries_url)
json_file2 = get_available_countries.json()
print(json_file2)

# Long Weekend
year = 2023
weekends_url = "https://date.nager.at/api/v3/LongWeekend/{year}/{country_code}"
get_weekends = requests.get(weekends_url)
json_file3 = get_weekends.json()
print(json_file3)

# Public Holiday

# et Public Holidays
