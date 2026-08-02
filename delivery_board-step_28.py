# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: DeliveryBoard
def print_delivery_metrics():
    """Компактный блок метрик: количество заказов, активных курьеров, статусы, средняя длительность."""
    stats = {
        "total_orders": len(orders),
        "active_couriers": sum(1 for c in couriers if not c["busy"]),
        "completed_deliveries": sum(1 for o in orders if o["status"] == "delivered"),
        "in_progress": sum(1 for o in orders if o["status"] in ("pending", "in_transit")),
    }
    durations = [o["duration_min"] for o in orders if o.get("duration_min") and o["status"] != "scheduled"]
    stats["avg_delivery_time_min"] = round(sum(durations) / len(durations), 1) if durations else 0
    print(f"📦 Всего заказов: {stats['total_orders']}")
    print(f"🚴 Активные курьеры: {stats['active_couriers']}/{len(couriers)}")
    print(f"✅ Доставлено: {stats['completed_deliveries']}")
    print(f"🔄 В процессе: {stats['in_progress']}")
    print(f"⏱ Среднее время доставки: {stats['avg_delivery_time_min']} мин")
