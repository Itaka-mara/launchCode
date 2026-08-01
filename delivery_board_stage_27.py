# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: DeliveryBoard
def reset_demo_data():
    """Reset all data to demo state."""
    global orders, routes, couriers, statuses, deadlines, active_orders, completed_orders
    orders = [
        {"id": 1, "customer": "Alex", "item": "Pizza", "address": "Main St 10", "status": "delivered"},
        {"id": 2, "customer": "Bella", "item": "Sushi", "address": "Oak Ave 5", "status": "in_transit"},
        {"id": 3, "customer": "Charlie", "item": "Salad", "address": "Park Rd 12", "status": "pending"},
    ]
    routes = [
        {"from": "Main St 10", "to": "Oak Ave 5", "distance_km": 3.5},
    ]
    couriers = ["Mike", "Lisa", "Tom"]
    statuses = ["pending", "preparing", "in_transit", "delivered", "cancelled"]
    deadlines = [
        {"order_id": 1, "deadline": "2026-07-15T18:30"},
        {"order_id": 2, "deadline": "2026-07-14T20:00"},
    ]
    active_orders = [i for i in orders if i["status"] not in ("delivered", "cancelled")]

def clear_state():
    """Clear all data."""
    global orders, routes, couriers, statuses, deadlines, active_orders, completed_orders
    orders = []
    routes = []
    couriers = []
    statuses = []
    deadlines = []
    active_orders = []
    completed_orders = []

def load_demo():
    """Reset to demo and print status."""
    reset_demo_data()
    print(f"Demo loaded: {len(orders)} orders, {len(routes)} routes, {len(couriers)} couriers")
