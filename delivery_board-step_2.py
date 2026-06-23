# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: DeliveryBoard
class DeliveryModel:
    def __init__(self):
        self.orders = []
        self.couriers = []
        self.routes = []
        self.statuses = ["pending", "in_transit", "delivered", "cancelled"]

    def validate_order(self, data):
        if not isinstance(data.get('customer'), str) or len(data['customer']) < 2:
            return False, "Имя клиента должно быть строкой длиной не менее 2 символов"
        if not isinstance(data.get('address'), str) or len(data['address']) < 5:
            return False, "Адрес должен быть строкой длиной не менее 5 символов"
        if data.get('deadline') and (not isinstance(data['deadline'], int) or data['deadline'] <= 0):
            return False, "Срок доставки должен быть положительным целым числом"
        return True, None

    def validate_courier(self, data):
        if not isinstance(data.get('name'), str) or len(data['name']) < 2:
            return False, "Имя курьера должно быть строкой длиной не менее 2 символов"
        if not isinstance(data.get('phone'), str) or len(data['phone']) != 11:
            return False, "Номер телефона должен содержать ровно 11 цифр"
        return True, None

    def validate_route(self, data):
        if not self.validate_order(data):
            return False, "Неверные данные заказа в маршруте"
        if not isinstance(data.get('courier_id'), int) or data['courier_id'] < 0:
            return False, "ID курьера должен быть неотрицательным целым числом"
        return True, None

    def add_order(self, order_data):
        valid, error = self.validate_order(order_data)
        if not valid:
            raise ValueError(error)
        self.orders.append({**order_data, 'id': len(self.orders) + 1})

    def add_courier(self, courier_data):
        valid, error = self.validate_courier(courier_data)
        if not valid:
            raise ValueError(error)
        self.couriers.append({**courier_data, 'id': len(self.couriers) + 1})

    def add_route(self, route_data):
        valid, error = self.validate_route(route_data)
        if not valid:
            raise ValueError(error)
        self.routes.append({**route_data, 'id': len(self.routes) + 1})
