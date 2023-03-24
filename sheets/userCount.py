import os.path
from pprint import pprint
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
import re

#Parameters
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1utT4pdhWvnwdfr5zt1nPeS61XWMy_gqabkokO6XG7AE'


def get_user_count():
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
  return number_of_users