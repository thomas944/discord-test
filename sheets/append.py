import os.path
import sys
from pprint import pprint
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from datetime import date
from test3 import get_tweets_intoDF, showPercentage, best, wordCloud
from userCount import get_user_count


# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'

#Parameters
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1utT4pdhWvnwdfr5zt1nPeS61XWMy_gqabkokO6XG7AE'
RANGES = 'A4:M4'  
VALUE_INPUT_OPTION = 'RAW'
INSERT_DATA_OPTION = 'INSERT_ROWS'
INCLUDE_VALUES_IN_RESPONSE = 'true'
RESPONSE_DATE_TIME_RENDER_OPTION = 'FORMATTED_STRING'

def add_user_to_database(user, followers, following, tweets):
  os.chdir('/Users/pham/Desktop/Coding/Project/discord-bot/sheets')
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  service = discovery.build('sheets', 'v4', credentials=creds)
  tweets_array = showPercentage()
  print(tweets_array[0])
  print(tweets_array[1])
  print(tweets_array[-1])

  value_range_body = {
    "values": [
      [
        user, #username
        followers, #followers
        following, #following
        tweets, #tweets analyzed
        1,
        str(date.today()), #most recent search
        str(tweets_array[-1]), #negative
        str(tweets_array[1]), #positive
        str(tweets_array[0]), #neutral
        str(best('positive')), #best tweet
        str(best('negative')), #worst tweet
        str(wordCloud('positive')), #dict positive
        str(wordCloud('negative')), #dict negative
      ]
    ],    
    "range": "A4:M4",
    "majorDimension": "ROWS"
  }

  request = service.spreadsheets().values().append(
    spreadsheetId = SPREADSHEET_ID,
    range = RANGES,
    includeValuesInResponse = INCLUDE_VALUES_IN_RESPONSE,
    insertDataOption = INSERT_DATA_OPTION,
    responseDateTimeRenderOption = RESPONSE_DATE_TIME_RENDER_OPTION,
    valueInputOption = VALUE_INPUT_OPTION,
    body = value_range_body
  )
  response = request.execute()
  


  # TODO: Change code below to process the `response` dict:
  pprint(response)

add_user_to_database("elonmusk",1000, 1000, 1000)