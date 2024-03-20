from bs4 import BeautifulSoup
import requests
import html5lib

source = requests.get("https://quotes.toscrape.com").text
soup = BeautifulSoup(source, "lxml")

for i in soup.find_all('small', class_="author"):
    print(i.text.strip())

for j in soup.find_all('div', class_="quote"):
    print(j.span.text.strip())

