from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Exercises/Mar21Exercises/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# this has the driver wait until an html element is visible 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

#this finds that element 
#this is a search bar 
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

#this clears it to ensure it is empty
input_element.clear()


#this types in text into the search bar & then presses enter
input_element.send_keys("tech with tim" + Keys.ENTER)

#now waiting for the link to appear 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

#then finding that link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")

#think clicking that link
link.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]"))
)

link2 = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]")

link2.click()

time.sleep(10)

#closes the entire browser
driver.quit()