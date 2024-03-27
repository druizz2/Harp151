from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd

new_csv = open("libcongress.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(new_csv)
csv_writer.writerow(["Title", "Item Desciption", "Hyperlink"])

page = 1
# title, item description, webpage hyperlink, all into csv
while page != 6:
    source = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}").text
    soup = BeautifulSoup(source, "lxml")

    for element in soup.find_all("div", class_="description"):
        title = element.a.text.strip()

        try:
            item_description = element.find("span", class_="item-description-abstract").text.strip()
        except AttributeError:
            print(f"No item description for {title}")

        hyperlink = element.a.get('href')
        csv_writer.writerow([title, item_description, hyperlink])
    page += 1 

sheet = pd.read_csv("libcongress.csv")
