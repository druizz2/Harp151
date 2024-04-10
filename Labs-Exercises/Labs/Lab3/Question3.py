import requests 
import json

# sources | https://stackoverflow.com/questions/27315472/how-to-count-items-in-json-data
# -> used for figuring out how to get number of elements in a json object

def count_public_holidays():
    try: 
        country_code = str(input("Enter a country code. "))
        year = int(input("\nEnter a year. "))
        base_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
        get_holidays_count = requests.get(base_url)
        holidays_count_json = get_holidays_count.json()
        number_of_public_holidays = len(holidays_count_json)
        return number_of_public_holidays
    except ValueError:
        print("No Available public holidays, try again.")
        count_public_holidays()
count_public_holidays()