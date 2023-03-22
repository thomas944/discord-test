import os.path
from pprint import pprint
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
import re


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
DATE_TIME_RENDER_OPTION = 'FORMATTED_STRING'
MAJOR_DIMENSION = 'ROWS'
VALUE_RENDER_OPTION = 'FORMATTED_VALUE'
RANGE = 'A11:E11'
BEGIN_OF_LIST = 4


def search_for_user(userName):
  print(os.getcwd())
  os.chdir('/Users/pham/Desktop/Coding/Project/discord-bot/sheets')
  print(os.getcwd())

  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

  service = discovery.build('sheets', 'v4', credentials=creds)

  request = service.spreadsheets().values().get(
    spreadsheetId = SPREADSHEET_ID,
    range = 'C1'
  )
  response = request.execute()
  temp = (re.sub("[^0-9]", "", str(str(response).split(',')[2].split(':'))))
  number_of_users = (int(temp.strip('\"')))
  for i in range(BEGIN_OF_LIST, BEGIN_OF_LIST+number_of_users):
    RANGE = f'A${i}:E${i}'
    request = service.spreadsheets().values().get(
      spreadsheetId = SPREADSHEET_ID,
      range = RANGE,
      dateTimeRenderOption = DATE_TIME_RENDER_OPTION,
      majorDimension = MAJOR_DIMENSION,
      valueRenderOption = VALUE_RENDER_OPTION
    )
    response = request.execute()
    temp =  str(response).split(',')[2].split(':')[1]

    replacements = [('"',""),("'",""),("\[",""),("\]",""),(" ","")]
    for char, repl in replacements:
      temp = re.sub(char, repl, temp)
    #temp =  str(response).split(',')[2].split(':')[1]
    usernames = temp.strip('\"')
    if userName == usernames:
      return i
    

search_for_user("ngoc")