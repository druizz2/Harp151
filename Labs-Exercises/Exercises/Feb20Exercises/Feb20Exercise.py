import json
import requests
import csv

lat = "42.098701"
lon = "-75.912537"
weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

json_file = weather.json()
print(json.dumps(json_file, indent=3))
print(json_file.keys())

api_key = "7bcc064dc97cae180252585ad34dd7d8407ad18c"
url = f"https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*&key={api_key}"
census_data = requests.get(url)
json_file2 = census_data.json()
print(json_file2)

csv_file = open("json_data.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
for i in json_file2:
    csv_writer.writerow(i)
csv_file.close()
