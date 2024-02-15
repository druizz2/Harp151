import requests 
import json
import csv
import pandas as pd 

key = "7bcc064dc97cae180252585ad34dd7d8407ad18c"
url = f"https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*&key={key}"

census_data = requests.get(url)
json_file = census_data.json()

json_file