from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
import nltk


BASE_URL = "https://www.gutenberg.org/ebooks/"
SEARCH_BAR = "book-search"
BOOK_LINK = "booklink"
#BOOK_FORMAT = "Plain Text UTF-8"
BOOK_FORMAT_HTML = "Read this book online: HTML5"
FILE_NAME = "temp.txt"
FILE_OPERATION = "w"

def getData(bookName):
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get(BASE_URL)

  driver.implicitly_wait(5)

  try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, SEARCH_BAR))
    )
    element.clear()
    element.send_keys(bookName)
    element.send_keys(Keys.RETURN)
      
    element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, BOOK_LINK))
    ) 
    element.click()
    element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.LINK_TEXT, BOOK_FORMAT_HTML))
    )
    element.click()
    chapters = driver.find_elements(By.CLASS_NAME,"chapter")

    myFile = open(FILE_NAME,FILE_OPERATION)
    i = 0
    while(i<len(chapters)):
      myFile.write(chapters[i].text)
      i+=1
    myFile.close()
    
  finally:
    driver.quit()


def createDF():
  sia = SIA()
  results = []
  
  myFile = open("temp.txt", "r")
  for paragraph in myFile:
    if(paragraph.find("Chapter") != -1):
      continue 
    pol_score = sia.polarity_scores(paragraph)
    pol_score['paragraph'] = paragraph
    results.append(pol_score)
     
  df = pd.DataFrame.from_records(results)
  df['label'] = 0
  df.loc[df['compound'] > 0.2, 'label'] = 1
  df.loc[df['compound'] < -0.2, 'label'] = -1
  df.to_csv('book.csv', encoding='utf-8')
  return df


getData('northanger Abbey')