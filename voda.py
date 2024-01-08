import os
import sms
from google.auth import credentials
from google.auth.transport.requests import Requests

# Set up Vodafone API credentials
vodafone_credentials = credentials.JSONCredentials(os.environ.get('VODAFONE_CREDENTIALS'))
vodafone_client = sms.VodafoneSMSClient(vodafone_credentials.api_key,
                                         vodafone_credentials.api_secret)

# Set up Google Form API credentials
google_credentials = credentials.JSONCredentials(
    os.environ.get('GOOGLE_CREDENTIALS'))
google_client = requests.client('https://www.googleapis.com/auth/spreadsheets')

# Define the spreadsheet to which the link will be sent
spreadsheet_id = 'YOUR_SPREADSHEET_ID'
spreadsheet = google_client.spreadsheet(spreadsheet_id)

# Define the message to be sent
message = 'Hello, ' '.' + '! Please fill out the following form'

# Send the message
response = vodafone_client.sms_send(message, [('010-234567891', '0123456789'), ('911122223', '123456')],
                                     headers={"X-Vodafone-Message-ID": message})

# Check the response
if response.status_code == 200:
    # The link has been sent, and the user can click it to fill out the form in Google Sheets.
    print(f'Message sent successfully!')
else:
    print(f'Error occurred: {response.status_code} {response.reason}')
