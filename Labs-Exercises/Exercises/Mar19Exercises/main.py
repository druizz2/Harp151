from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

source = requests.get("https://books.toscrape.com/catalogue/page-1.html").text
soup = BeautifulSoup(source, "lxml")

# print(soup)

# for i in soup.find_all('p', class_="price_color"):
#     print(i.text.strip('Â'))
# # h3 for book titles 
# for j in soup.find_all('h3'):
#     print(j.a.text.strip())

# books_dict = {}
# for number in range(50):
#     for j in soup.find_all('h3'):
#         titles = j.a.text.strip()
#         for i in soup.find_all('p', class_="price_color"):
#             prices = i.text.strip('Â')
#         books_dict[titles] = prices

# print(books_dict)
new_csv = open("books_scrape.csv", "w", newline="", encoding = "utf-8")
csv_writer = csv.writer(new_csv)
csv_writer.writerow(["Title", "Price"])

page = 1
while page != 4:
    books=requests.get(f"https://books.toscrape.com
                       /catalogue/page--{page}.html".text)
    soup = BeautifulSoup(books, "lxml")
    page += 1

    for i in books.find_all("article", class_="product_pod"):
        title = i.h3.a["title"]
        price = i.find("p", class_="price_color").text.strip("Â")
        csv_writer.writerow([title, price])
    page+=1
sheet4 = pd.read_csv("books_scrape.csv")

"""
The project is moving along well. We are finalizing our decisions on the 
minigames we want to implement as well as finalizing our user interview
questions. 
"""