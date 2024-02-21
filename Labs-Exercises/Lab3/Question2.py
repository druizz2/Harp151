import requests
import json  

base_url = "https://date.nager.at/api/v3/"
country_code = "AU"
year = 2023

# Country

# Get Country info -> Returns country specific info based on country code

country_url = f"https://date.nager.at/api/v3/CountryInfo/{country_code}"
get_country_info = requests.get(country_url)
json_file = get_country_info.json()
# print(json_file)

# Available Countries -> Returns all countries in API

available_countries_url = f"https://date.nager.at/api/v3/AvailableCountries"
get_available_countries = requests.get(available_countries_url)
json_file2 = get_available_countries.json()
# print(json_file2)


# Long Weekend

weekends_url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{country_code}"
get_weekends = requests.get(weekends_url)
json_file3 = get_weekends.json()
# print(json_file3)


# Public Holiday

# Get Public Holidays
holiday_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
get_holidays = requests.get(holiday_url)
json_file4 = get_holidays.json()
print(json_file4)

# Is Today a Public Holiday -> Checks if today is a public holiday in country code
public_holiday_check_url = f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{country_code}"
get_holiday_check = requests.get(public_holiday_check_url)
# json_file5 = get_holiday_check.json() -> in comments because it returns an empty JSON, causing an error 
# print(json_file5)

# Next Public Holiday -> Returns next public holdiay for specific country code 
next_holiday_url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}"
get_next_holiday = requests.get(next_holiday_url)
json_file6 = get_next_holiday.json()
# print(json_file6)

# Next Public Holidays Worldwide -> Returns next public holiday worldwide
next_holiday_world_url = "https://date.nager.at/api/v3/NextPublicHolidaysWorldwide"
get_next_holiday_world = requests.get(next_holiday_world_url)
json_file7 = get_next_holiday_world.json()
# print(json_file7)