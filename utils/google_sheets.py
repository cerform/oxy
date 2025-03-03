import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
SHEET_NAME = "Nitrogen_Usage_Log"  # Change to your sheet name
CREDENTIALS_FILE = "data/credentials.json"  # Store your Google API credentials here

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).sheet1  # Access the first sheet

def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
