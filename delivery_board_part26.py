# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: DeliveryBoard
def demo_delivery_board():
    print("=== DeliveryBoard Demo ===")

    # Создаем статусы
    statuses = ["pending", "accepted", "in_progress", "delivered"]

    # Создаем курьеров
    couriers = [
        {"name": "Алексей", "status": "available"},
        {"name": "Мария", "status": "busy"},
    ]

    # Добавляем заказы
    orders = []

    for i in range(1, 6):
        order = {
            "order_id": f"ORD-{i:03d}",
            "customer": {"name": f"Клиент_{i}", "phone": f"+79{100 + i}**{i}"},
            "address": {"city": "Москва", "street": f"Улица {chr(65 + (i % 4))}{i // 4 + 1}", "house": 100 + i, "lat": 55.75 + (i * 0.01), "lng": 37.62 + (i * 0.01)},
            "status": statuses[i % len(statuses)],
            "priority": {"level": 1 if i <= 2 else 2},
            "courier": couriers[0] if i <= 2 else couriers[1],
            "created_at": f"2024-01-{5 + (i % 20):02d}T10:00:00",
            "delivery_date": f"2024-01-{8 + (i % 20):02d}T18:00:00",
        }
        orders.append(order)

    # Выводим заказы
    print(f"\nЗаказов: {len(orders)}")
    for order in orders:
        print(f"  - {order['order_id']}: {order['customer']['name']} — {order['address']['street']} | Статус: {order['status']}")

    # Выводим статусы
    print("\nСтатусы:")
    for s in statuses:
        print(f"  - {s}")

    # Выводим курьеров
    print("\nКурьеры:")
    for c in couriers:
        print(f"  - {c['name']}: статус — {c['status']}")

    print("\n=== Демо завершён ===")
