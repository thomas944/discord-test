import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

INPUT = "@elonmusk"
WEB_URL = "https://twitter.com/"
SEARCH_BAR = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-y0fyvk r-1dz5y72 r-fdjqy7 r-13qz1uu"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(WEB_URL)
driver.implicitly_wait(5)

element = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//input[@placeholder = "Search Twitter"]')))
element.clear()
element.send_keys(INPUT)
element.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.LINK_TEXT, INPUT))
)
element.click()
time.sleep(2)


one = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[5]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div"
two = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[5]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time"
# scrolling = True
#   while scrolling:
#   tweets = WebDriverWait(driver, 5).until
#user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')))
#date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, one)))

myFile = open('db.txt','w')
scrolling = True
while scrolling:
  tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid = "tweet"]')
  for tweet in tweets: 
    data = tweet.text.split('\n')
    myFile.write(str(data) + '\n')
    print(data)
    

  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
      # Scroll down to bottom
      driver.execute_script(f"window.scrollTo(0, {last_height+20000});")
      # Wait to load page
      time.sleep(2)
      # Calculate new scroll height and compare it with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      # check if the date substring from above is in the date list, condition 1
      
      # condition 2
      if new_height == last_height:
          scrolling = False
          break

      else:
          last_height = new_height
          break
