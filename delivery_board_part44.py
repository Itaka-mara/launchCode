# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: DeliveryBoard
import os, json, shutil, datetime

def backup_data_file(file_path):
    if not os.path.exists(file_path):
        return
    backup_dir = os.path.join(os.path.dirname(file_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    now = datetime.datetime.now()
    backup_name = f"backup_{now.strftime('%Y%m%d_%H%M%S')}.json"
    backup_path = os.path.join(backup_dir, backup_name)
    shutil.copy2(file_path, backup_path)
    print(f"Backup saved to {backup_path}")

backup_data_file("delivery_data.json")
