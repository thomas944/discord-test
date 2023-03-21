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
RANGES = 'A2:E2'  
VALUE_INPUT_OPTION = 'RAW'
INSERT_DATA_OPTION = 'INSERT_ROWS'
INCLUDE_VALUES_IN_RESPONSE = 'true'
RESPONSE_DATE_TIME_RENDER_OPTION = 'FORMATTED_STRING'


if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = discovery.build('sheets', 'v4', credentials=creds)


value_range_body = {
  "values": [
    [
      "T",
      "h",
      "o",
      "m",
      "a"
    ]
  ],    
  "range": "A2:E2",
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