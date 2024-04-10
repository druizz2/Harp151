from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# creating driver to open
driver = webdriver.Edge()

# settng driver to page
driver.get("https://www.wikipedia.org/")

# this has the driver wait until an html element is visible (input)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input"))
)
# finds html input element
input_element = driver.find_element(By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input")

# clears the input element
input_element.clear()

# types in dog and presses enter
input_element.send_keys("dog" + Keys.ENTER)

# for loop to search the page for h2 elements
for element in driver.find_elements(By.TAG_NAME, "h2"):
    # assigrning each found element to h2, extracting the text
    h2 = element.text
    print(h2)

# waits 10 seconds to sleep the driver
time.sleep(10)
# then quits the driver page
driver.quit()