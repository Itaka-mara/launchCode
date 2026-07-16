# === Stage 17: Добавь группировку записей по категориям ===
# Project: DeliveryBoard
def group_by_category(items, key_fn):
    groups = {}
    for item in items:
        cat = key_fn(item)
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(item)
    return groups
