import os
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets setup
SHEET_NAME = "Nitrogen_Usage_Log"  # Укажи название своего листа
CREDENTIALS_FILE = "data/credentials.json"  # Путь к файлу с API-ключами

def connect_to_sheets():
    """ Подключается к Google Sheets и возвращает объект листа """
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"Файл {CREDENTIALS_FILE} не найден. Проверь путь!")

    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open(SHEET_NAME).sheet1  # Открываем первый лист
        return sheet
    except Exception as e:
        print(f"Ошибка подключения к Google Sheets: {e}")
        return None

def add_entry_to_sheets(data):
    """ Добавляет строку в Google Sheets """
    sheet = connect_to_sheets()
    if sheet:
        try:
            sheet.append_row(data)
            print("✅ Данные успешно добавлены в Google Sheets!")
        except Exception as e:
            print(f"❌ Ошибка при добавлении данных: {e}")
