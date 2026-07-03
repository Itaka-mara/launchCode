# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: DeliveryBoard
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация обязательных полей
        required_keys = ['orders', 'couriers', 'routes']
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует ключ '{key}'")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Ключ '{key}' должен быть списком")
        
        # Пример валидации структуры заказа (можно расширить)
        for order in data['orders']:
            if 'id' not in order or 'status' not in order:
                raise ValueError("Некорректная структура заказа")
                
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (замените эту строку на вашу переменную с данными):
initial_data = load_initial_data('{"orders": [{"id": 1, "status": "pending"}], "couriers": [], "routes": []}')
