from bs4 import BeautifulSoup
import requests
import html5lib

source = requests.get("https://www.loc.gov/search/?q=cats&sp=1")
soup = BeautifulSoup(source, "lxml")

page = 1

while page != 6:
    pass