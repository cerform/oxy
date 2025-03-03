import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "Nitrogen_Usage_Log"

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials_json = os.getenv("GOOGLE_CREDENTIALS")  # Берем JSON из переменной окружения

    if not credentials_json:
        raise FileNotFoundError("Переменная GOOGLE_CREDENTIALS не найдена!")

    credentials_dict = json.loads(credentials_json)  # Преобразуем JSON-строку в словарь
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)  # Создаем креды
    client = gspread.authorize(creds)

    return client.open(SHEET_NAME).sheet1  # Открываем Google Sheets

def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
