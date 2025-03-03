import os
import gspread
from google.oauth2.service_account import Credentials

SHEET_NAME = "Nitrogen_Usage_Log"

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Путь к секретному файлу
    creds_path = '/etc/secrets/credentials.json'

    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Секретный файл не найден по пути {creds_path}")

    # Создаем учетные данные Google
    creds = Credentials.from_service_account_file(creds_path, scopes=scope)
    client = gspread.authorize(creds)

    return client.open(SHEET_NAME).sheet1

def add_entry_to_sheets(data):
    sheet = connect_to_sheets()
    sheet.append_row(data)
