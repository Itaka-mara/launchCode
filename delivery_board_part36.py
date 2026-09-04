# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: DeliveryBoard
def check_and_repair_integrity():
    """Проверка целостности данных и ремонт простых проблем."""
    issues = []
    if not orders or not routes or not couriers or not statuses:
        issues.append("Missing top-level data structures")
        return issues

    # Проверка, что все заказанные товары есть в инвентаре
    order_items = [item for order in orders for item in order.get("items", [])]
    inventory_items = [item for item in inventory.values() for _ in item]
    missing_items = set(order_items) - set(inventory_items)
    if missing_items:
        issues.append(f"Missing items: {missing_items}")
        return issues

    # Проверка, что все статусы используются корректно
    for order in orders:
        status = order.get("status")
        if status not in statuses:
            issues.append(f"Invalid status: {status}")

    # Проверка, что все маршруты корректно назначены
    for route in routes:
        if route.get("courier") not in [c["name"] for c in couriers]:
            issues.append(f"Route has unknown courier: {route.get('courier')}")

    # Проверка, что все заказы привязаны к маршруту
    for order in orders:
        if order.get("route") not in [r["name"] for r in routes]:
            issues.append(f"Order has unknown route: {order.get('route')}")

    # Проверка, что все курьеры назначены на маршрут
    for courier in couriers:
        if courier.get("route") not in [r["name"] for r in routes]:
            issues.append(f"Courier has unknown route: {courier.get('route')}")

    return issues

def repair_simple_problems():
    """Ремонт простых проблем."""
    if not orders or not routes or not couriers or not statuses:
        print("Cannot repair: missing data structures")
        return

    # Исправление статусов, которые не существуют
    for order in orders:
        if order.get("status") not in statuses:
            order["status"] = statuses[0]["name"]

    # Исправление маршрутов, которые не существуют
    for order in orders:
        if order.get("route") not in [r["name"] for r in routes]:
            order["route"] = routes[0]["name"]

    # Исправление курьеров, которые не существуют
    for route in routes:
        if route.get("courier") not in [c["name"] for c in couriers]:
            route["courier"] = couriers[0]["name"]
