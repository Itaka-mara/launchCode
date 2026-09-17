# === Stage 45: Добавь восстановление из резервной копии ===
# Project: DeliveryBoard
def restore_from_backup(filepath):
    if not filepath or not os.path.exists(filepath):
        print(f"Резервная копия не найдена: {filepath}")
        return False
    with open(filepath, 'r') as f:
        data = json.load(f)
    for key in data:
        globals()[key] = data[key]
    print(f"Резервная копия успешно восстановлена из {filepath}")
    return True
