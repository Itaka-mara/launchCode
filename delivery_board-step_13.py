# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: DeliveryBoard
def search_orders(query: str) -> list[dict]:
    """Поиск заказов по нескольким полям без учёта регистра."""
    q = query.lower()
    results = []
    for order in orders:
        if (q in order['order_id'].lower() or
            q in order['status'].lower() or
            q in order['delivery_address'].lower()):
            results.append(order)
    return results
