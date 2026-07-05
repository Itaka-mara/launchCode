# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: DeliveryBoard
def export_to_json():
    import json
    state = {
        "orders": orders,
        "routes": routes,
        "couriers": couriers,
        "statuses": statuses,
        "timestamp": datetime.now().isoformat() if 'datetime' in globals() else None
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
