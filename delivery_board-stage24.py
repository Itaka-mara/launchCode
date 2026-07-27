# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: DeliveryBoard
def print_delivery_record(record):
    """Компактный вывод одной записи доставки."""
    if not record:
        return
    name = record.get('name', 'Без имени')
    status = record.get('status', 'Неизвестен')
    deadline = str(record.get('deadline', ''))
    route_type = record.get('route_type', 'Нет маршрута')
    courier_name = record.get('courier', {}).get('name', 'Нет курьера' if isinstance(record.get('courier'), dict) else 'Не назначен')
    print(f"=== Запись доставки: {name} ===")
    print(f"Статус: {status}")
    print(f"Дедлайн: {deadline}")
    print(f"Тип маршрута: {route_type}")
    if isinstance(record.get('courier'), dict):
        print(f"Курьер: {courier_name}")
