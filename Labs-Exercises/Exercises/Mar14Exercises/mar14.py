from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd


source = requests.get("https://www.scrapethissite.com/pages/").text
soup = BeautifulSoup(source, "lxml")
# # print(soup.prettify())
# soup.find_all("div", class_="col-md-6 col-md-offset-3")
# # soup.body.div.a
# div_page = soup.find('div', class_= 'page')
# div_page
# pbox = div_page.find('p').text
# pbox
empty_soup = soup.find('div', class_="col-md-6 col-md-offset-3")

csv_file = open('cms_scrape.csv', "w")

for element in empty_soup.find_all("div", class_="page"):
  title = element.a.text
  desc = element.p.text.strip()
  print(title, "|", desc)

# .strip take out white space and characters 
pd.read_csv('cms_scrape.csv')
