# from selenium import webdriver
# import time

# PATH = "chromedriver_mac_arm64/chromedriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://google.com")
# print(driver.get_cookies())
# time.sleep(5)
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
time.sleep(5)