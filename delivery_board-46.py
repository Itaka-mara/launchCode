# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: DeliveryBoard
MIGRATION_LOG = []

def migrate(version):
    global MIGRATION_LOG
    if version not in MIGRATION_LOG:
        MIGRATION_LOG.append(version)
        print(f"Applied migration v{version}: {MIGRATION_LOG[-1]}")
    return MIGRATION_LOG

# Пример: миграция добавляет новый статус "В пути"
migrate(46)
