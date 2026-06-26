# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: DeliveryBoard
def edit_delivery_record(record_id, updates):
    if record_id not in deliveries:
        raise ValueError(f"Запись с ID {record_id} не найдена")
    
    for key, value in updates.items():
        if key == 'status':
            valid_statuses = ['new', 'in_progress', 'completed', 'cancelled']
            if value not in valid_statuses:
                raise ValueError(f"Неверный статус. Доступные: {valid_statuses}")
        
        # Обновляем поля, если они не являются внутренними (например, id)
        if key != 'id':
            deliveries[record_id][key] = value
    
    return deliveries[record_id]
