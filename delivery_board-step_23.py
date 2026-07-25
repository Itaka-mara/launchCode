# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: DeliveryBoard
def print_board_table(board):
    """Выводит доску доставок в компактной табличной форме."""
    if not board:
        print("Доска пуста")
        return

    headers = ["ID", "Статус", "Заказчик", "Курьер", "Срок"]
    widths = [10, 25, 18, 18, 14]
    for h, w in zip(headers, widths):
        print(h.ljust(w))

    print("-" * sum(widths))

    for order in board:
        row = []
        row.append(str(order["id"]).ljust(10))
        status_map = {"new": "Новый", "in_progress": "В пути", "completed": "Готов"}
        row.append(status_map.get(order["status"], str(order["status"])).ljust(25))
        row.append(str(order.get("client", "")).ljust(18))
        courier = order.get("courier", {}).get("name", "") if isinstance(order.get("courier"), dict) else ""
        row.append(str(courier).ljust(18))
        row.append(str(order.get("deadline", "—")).ljust(14))

        print("\t".join(row))
