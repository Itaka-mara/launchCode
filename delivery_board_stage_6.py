# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: DeliveryBoard
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            record_tags = set(record.get('tags', []))
            if not any(tag in record_tags for tag in tags):
                continue
        filtered.append(record)
    return filtered
