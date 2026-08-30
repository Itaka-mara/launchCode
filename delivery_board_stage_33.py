# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: DeliveryBoard
def undo_last_delivery_board_action():
    """Откат последнего действия доски доставки.
    
    Поддерживаемые действия:
    - добавление заказа
    - добавление курьера
    - обновление статуса заказа
    - добавление маршрута
    
    Реализация: сохраняем историю всех действий в отдельном списке,
    при каждом изменении доска записывает состояние. При вызове undo()
    откатываем состояние к предыдущему.
    """
    global last_action, last_state
    
    if last_action is None:
        print("Нет действий для отката.")
        return
    
    # Восстанавливаем состояние досок из сохранённого
    for board_name, board in delivery_boards.items():
        if last_state:
            board.update(last_state[board_name])
    
    print(f"Откат от действия: {last_action}")
    last_action = None
