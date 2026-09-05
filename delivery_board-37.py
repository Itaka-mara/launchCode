# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: DeliveryBoard
import unittest
from delivery_board import (
    Order, Route, Courier, Status, Delivery, Board,
    create_order, create_route, create_courier, create_status,
    create_delivery, create_board
)

class TestDeliveryBoard(unittest.TestCase):

    def test_create_order(self):
        o = create_order("ORD001", "Test Customer", "Street 1", 100)
        self.assertEqual(o.order_id, "ORD001")
        self.assertEqual(o.customer, "Test Customer")
        self.assertEqual(o.items, 100)

    def test_create_route(self):
        r = create_route("R1", "A", "B", 50)
        self.assertEqual(r.route_id, "R1")
        self.assertEqual(r.start, "A")
        self.assertEqual(r.end, "B")
        self.assertEqual(r.distance, 50)

    def test_create_courier(self):
        c = create_courier("C1", "Courier A", 20)
        self.assertEqual(c.courier_id, "C1")
        self.assertEqual(c.name, "Courier A")
        self.assertEqual(c.speed, 20)

    def test_create_status(self):
        s = create_status("S1", "Pending")
        self.assertEqual(s.status_id, "S1")
        self.assertEqual(s.name, "Pending")

    def test_create_delivery(self):
        d = create_delivery("D1", "ORD001", "C1")
        self.assertEqual(d.delivery_id, "D1")
        self.assertEqual(d.order_id, "ORD001")
        self.assertEqual(d.courier_id, "C1")

    def test_create_board(self):
        b = create_board()
        self.assertIsInstance(b, Board)

    def test_order_with_route(self):
        order = create_order("O1", "C", "S", 50)
        route = create_route("R1", "S", "D", 10)
        self.assertEqual(order.order_id, "O1")
        self.assertEqual(route.route_id, "R1")

    def test_delivery_with_route(self):
        delivery = create_delivery("DL1", "O1", "C1")
        route = create_route("R1", "A", "B", 5)
        self.assertEqual(delivery.delivery_id, "DL1")
        self.assertEqual(route.route_id, "R1")

    def test_board_creation(self):
        board = create_board()
        self.assertIsNotNone(board)

    def test_courier_speed(self):
        courier = create_courier("C2", "Fast Courier", 30)
        self.assertEqual(courier.speed, 30)

    def test_order_items(self):
        order = create_order("O2", "C2", "S2", 200)
        self.assertEqual(order.items, 200)

    def test_route_distance(self):
        route = create_route("R2", "X", "Y", 75)
        self.assertEqual(route.distance, 75)

if __name__ == '__main__':
    unittest.main()
