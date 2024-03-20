from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd

source = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(source, "lxml")
empty_soup = soup.find("div", class_="lister list detail sub-list")

new_csv = open("movies_scrape.csv","w", newline="", encoding = "utf-8")
csv_writer = csv.writer(new_csv)
csv_writer.writerow(["Title", "Release Date", "Score"])
 

for i in empty_soup.find_all("div", class_="lister-item mode-detail"):
        title = i.h3.a.text.strip()
                "span",class_="lister-item-year text-muted unbold").text.strip()
        metascore = i.find("span", class_="ipl-rating-star__rating").text.strip()
        csv_writer.writerow([title, release_year, metascore])

sheet = pd.read_csv("movies_scrape.csv")
