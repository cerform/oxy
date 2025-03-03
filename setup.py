import os

# Директории
dirs = [
    "utils",
    "templates",
    "static/css",
    "static/js",
    "data"
]

# Файлы
files = {
    "app.py": """# Flask сервер
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
    "requirements.txt": "Flask\ngspread\noauth2client",
    "config.py": "# Настройки Google Sheets API",
    "utils/google_sheets.py": """# Работа с Google Sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
    client = gspread.authorize(creds)
    return client
""",
    "templates/index.html": "<!-- HTML форма -->",
    "static/css/styles.css": "/* Стили */",
    "static/js/script.js": "// JS код",
    "data/departments.json": "{}"
}

# Создание директорий
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Создание файлов
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Проектная структура создана!")
