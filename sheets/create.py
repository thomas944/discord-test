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
credentials = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = '1utT4pdhWvnwdfr5zt1nPeS61XWMy_gqabkokO6XG7AE'


if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = discovery.build('sheets', 'v4', credentials=creds)

spreadsheet_body = {
  'properties': {
    'title': "Hello"
  }
}  
  


ranges = 'A2:E'  
include_grid_data = False  

request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=include_grid_data)
response = request.execute()
# request = service.spreadsheets().create(body=spreadsheet_body)
# response = request.execute()

# TODO: Change code below to process the `response` dict:
#f = open('test.txt',"a")
#f.write(str(response))
pprint(response)