from bs4 import BeautifulSoup
import requests
import html5lib

source = requests.get("https://tedboy.github.io/bs4_doc/1_quick_start.html").text
soup = BeautifulSoup(source, "lxml")

for i in soup.find_all('p'):
    print(i.text.strip())
    