import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

SHEET_NAME = "Nitrogen_Usage_Log"

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials_json = json.loads(os.getenv("GOOGLE_CREDENTIALS"))  # Уже правильно
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).sheet1  # Открываем первый лист таблицы

def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
