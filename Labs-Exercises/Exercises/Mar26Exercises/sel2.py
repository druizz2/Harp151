from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.scrapethissite.com/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div/ul/li[2]/a"))
)

link = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")

link.click()



for element in driver.find_elements(By.CSS_SELECTOR, "div.page"):
    desc = element.find_element(By.TAG_NAME, "p").text
    title = element.find_element(By.TAG_NAME, "h3").text
    print(title, "|", desc, "\n")
    
time.sleep(10)
driver.quit()


