from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get("https://www.wikipedia.org/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input"))
)
input_element = driver.find_element(By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input")

input_element.clear()

input_element.send_keys("cat" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/form/fieldset/div/div[2]/div/a[1]"))
)
link = driver.find_element(By.XPATH, "/html/body/main/div[2]/form/fieldset/div/div[2]/div/a[1]")


time.sleep(10)
driver.quit()

