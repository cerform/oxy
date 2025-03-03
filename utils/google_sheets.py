import os
import json
import base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "Nitrogen_Usage_Log"

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Читаем JSON из переменной окружения
    credentials_base64 = os.getenv("GOOGLE_CREDENTIALS_BASE64")

    if not credentials_base64:
        raise FileNotFoundError("Переменная GOOGLE_CREDENTIALS_BASE64 не найдена!")

    # Декодируем base64 в JSON
    credentials_json = base64.b64decode(credentials_base64).decode("utf-8")
    creds_dict = json.loads(credentials_json)

    # Создаем учетные данные Google
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    return client.open(SHEET_NAME).sheet1

def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
