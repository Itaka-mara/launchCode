# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: DeliveryBoard
import json, random
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional

@dataclass
class Order:
    id: int
    customer: str
    address: str
    status: str = "pending"
    deadline: datetime
    courier_id: Optional[int] = None

@dataclass
class Courier:
    id: int
    name: str
    current_order: Optional[Order] = None

def generate_demo_data() -> Dict[str, List]:
    orders = [
        Order(id=1, customer="Иванов И.И.", address="ул. Ленина 10", deadline=datetime.now() + timedelta(hours=2)),
        Order(id=2, customer="Петров П.П.", address="пр. Мира 5", status="in_transit", courier_id=1),
    ]
    couriers = [Courier(id=i+1, name=f"Курьер {i}") for i in range(3)]
    routes: List[Dict] = [{"from": "склад А", "to": "центр"}]
    statuses = ["pending", "in_transit", "delivered"]
    return {"orders": orders, "couriers": couriers, "routes": routes, "statuses": statuses}

if __name__ == "__main__":
    demo = generate_demo_data()
    print(json.dumps(demo, indent=2, default=str))
