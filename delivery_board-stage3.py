# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: DeliveryBoard
class DeliveryBoard:
    def __init__(self):
        self.orders = []
        self.couriers = []
        self.routes = []
    
    def add_order(self, order_id, customer, address, deadline):
        if any(o['id'] == order_id for o in self.orders):
            return False
        new_order = {'id': order_id, 'customer': customer, 'address': address, 'deadline': deadline, 'status': 'pending'}
        self.orders.append(new_order)
        return True
    
    def add_courier(self, courier_id, name, vehicle_type):
        if any(c['id'] == courier_id for c in self.couriers):
            return False
        new_courier = {'id': courier_id, 'name': name, 'vehicle_type': vehicle_type}
        self.couriers.append(new_courier)
        return True
    
    def add_route(self, route_id, start_address, end_address, estimated_time):
        if any(r['id'] == route_id for r in self.routes):
            return False
        new_route = {'id': route_id, 'start': start_address, 'end': end_address, 'estimated_time': estimated_time}
        self.routes.append(new_route)
        return True
