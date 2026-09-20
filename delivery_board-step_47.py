# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: DeliveryBoard
def demo():
    """Показать основной сценарий: создание заказов, курьеров, маршрутов и статусов."""
    from datetime import datetime, timedelta

    now = datetime.now()
    courier = Courier(name="Дмитрий", phone="+79001112233")
    orders = []

    # Заказы
    order1 = Order(
        customer="Анна",
        address="ул. Ленина 42",
        item="Пицца Маргарита",
        weight=0.5,
        price=450,
        deadline=now + timedelta(hours=1.5),
    )
    order2 = Order(
        customer="Борис",
        address="пр. Мира 108",
        item="Суши-сет",
        weight=1.2,
        price=890,
        deadline=now + timedelta(hours=2),
    )

    # Статусы
    statuses = [
        Status("new", "Новый"),
        Status("ready", "Готов к доставке"),
        Status("in_transit", "В пути"),
        Status("delivered", "Доставлен"),
    ]

    # Курьер на маршрут
    route = Route(
        courier=courier,
        statuses=statuses,
        orders=[order1, order2],
    )

    # Показать
    print(f"Курьер: {courier.name} ({courier.phone})")
    print(f"Маршрут: {len(route.orders)} заказов")
    for i, o in enumerate(route.orders, 1):
        print(f"  {i}. {o.customer} → {o.address} | {o.item} | {o.price}₽ (до {o.deadline})")
    print(f"Статусы: {[s.code for s in statuses]}")
