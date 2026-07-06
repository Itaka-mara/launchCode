# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: DeliveryBoard
import json, os

DB_FILE = "delivery_board.json"

def save_data(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data():
    if not os.path.exists(DB_FILE):
        return {"orders": [], "routes": [], "couriers": [], "statuses": []}
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key in ["orders", "routes", "couriers", "statuses"]:
            if key not in data:
                data[key] = []
        return data
    except (json.JSONDecodeError, IOError):
        return {"orders": [], "routes": [], "couriers": [], "statuses": []}
