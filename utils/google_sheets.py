import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "Nitrogen_Usage_Log"


def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "utils/credentials.json")

    if not os.path.exists(credentials_path):
        raise FileNotFoundError(
            f"Файл {credentials_path} не найден. Проверь путь или установи GOOGLE_APPLICATION_CREDENTIALS.")

    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)

    return client.open(SHEET_NAME).sheet1  # Открываем первый лист таблицы


def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
