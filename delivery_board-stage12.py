# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: DeliveryBoard
def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив")
        orders = []
        for item in data:
            required = ['order_id', 'customer', 'delivery_address']
            missing = [k for k in required if k not in item]
            if missing:
                print(f"Предупреждение: пропущено поле в {item.get('order_id','?')}: {missing}")
                continue
            orders.append(item)
        return orders
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON: {e}")
        return []
