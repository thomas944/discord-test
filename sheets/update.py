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


if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = discovery.build('sheets', 'v4', credentials=creds)

# The ID of the spreadsheet to update.
spreadsheet_id = 'my-spreadsheet-id'  # TODO: Update placeholder value.

# The A1 notation of the values to update.
range_ = 'my-range'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = ''  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body. All existing entries
    # will be replaced.
}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)