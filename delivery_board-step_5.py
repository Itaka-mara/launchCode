# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DeliveryBoard
def remove_order(order_id: int) -> bool:
    if order_id not in orders:
        print(f"Ошибка: заказ #{order_id} не найден.")
        return False
    del orders[order_id]
    # Очистка связанных маршрутов, если они существуют в глобальном списке
    routes_to_remove = [r for r in routes if r.order_id == order_id]
    for route in routes_to_remove:
        del routes[route['id']]
    print(f"Заказ #{order_id} успешно удален.")
    return True

def remove_courier(courier_id: int) -> bool:
    if courier_id not in couriers:
        print(f"Ошибка: курьер с ID {courier_id} не найден.")
        return False
    del couriers[courier_id]
    # Очистка активных назначений у удаленного курьера
    for route in routes.copy():
        if route['courier_id'] == courier_id and not route.get('completed'):
            print(f"Предупреждение: маршрут #{route['id']} был активным, но не завершен.")
            # Логика завершения или переназначения может быть добавлена здесь
    print(f"Курьер #{courier_id} успешно удален.")
    return True

def remove_route(route_id: int) -> bool:
    if route_id not in routes:
        print(f"Ошибка: маршрут #{route_id} не найден.")
        return False
    del routes[route_id]
    # Проверка на зависимость от заказа (опционально, если нужно обновлять статусы заказов)
    for order in orders.values():
        if order.get('status') == 'in_transit' and route_id in order.get('route_ids', []):
            print(f"Предупреждение: маршрут #{route_id} был частью активного заказа.")
    print(f"Маршрут #{route_id} успешно удален.")
    return True
