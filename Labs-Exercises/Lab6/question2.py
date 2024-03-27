from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd

# new_csv = open("cat.csv", "w", newline="", encoding="utf-8")
# csv_writer = csv.writer(new_csv)
# csv_writer.writerow(["Image Links"])

driver = webdriver.Edge()

driver.get("https://www.wikipedia.org/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input"))
)
input_element = driver.find_element(By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input")

input_element.clear()

input_element.send_keys("cat" + Keys.ENTER)



for element in driver.find_elements(By.CLASS_NAME, "mw-file-description"):
    image_links = element.get_attribute('href')
    print(image_links)
    # csv_writer.writerow([image_links])

# mw-file-description in an image tag or a href tag 

time.sleep(10)
driver.quit()

