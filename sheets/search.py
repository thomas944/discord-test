import os.path
from pprint import pprint
from googleapiclient import discovery
from google.oauth2.credentials import Credentials

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


if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = discovery.build('sheets', 'v4', credentials=creds)


request = service.spreadsheets().values().get(
  spreadsheetId = SPREADSHEET_ID,
  range = RANGE,
  dateTimeRenderOption = DATE_TIME_RENDER_OPTION,
  majorDimension = MAJOR_DIMENSION,
  valueRenderOption = VALUE_RENDER_OPTION
)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)