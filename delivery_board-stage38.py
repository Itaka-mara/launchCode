# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: DeliveryBoard
import unittest
from delivery_board import DeliveryBoard, Order, Courier, Route, Status

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.board = DeliveryBoard()
        self.board.add_courier(Courier("test", "T"))
        self.board.add_order(Order("o1", "C1", "A", "B", 100, 10))

    def test_duplicate_courier_id(self):
        with self.assertRaises(ValueError):
            self.board.add_courier(Courier("test", "T"))

    def test_duplicate_order_id(self):
        with self.assertRaises(ValueError):
            self.board.add_order(Order("o1", "C1", "A", "B", 100, 10))

    def test_add_order_without_courier(self):
        with self.assertRaises(ValueError):
            self.board.add_order(Order("o2", "C1", "A", "B", 100, 10))

    def test_remove_nonexistent_order(self):
        with self.assertRaises(ValueError):
            self.board.remove_order("o99")

    def test_negative_distance(self):
        with self.assertRaises(ValueError):
            self.board.add_order(Order("o3", "C1", "A", "B", -10, 10))

    def test_zero_distance(self):
        self.board.add_order(Order("o3", "C1", "A", "B", 0, 10))
        orders = self.board.get_orders()
        self.assertEqual(len(orders), 1)

    def test_zero_deadline(self):
        self.board.add_order(Order("o3", "C1", "A", "B", 10, 0))
        orders = self.board.get_orders()
        self.assertEqual(len(orders), 1)

    def test_negative_deadline(self):
        with self.assertRaises(ValueError):
            self.board.add_order(Order("o3", "C1", "A", "B", 10, -5))

    def test_remove_courier(self):
        self.board.remove_courier("test")
        couriers = self.board.get_couriers()
        self.assertEqual(len(couriers), 0)

    def test_remove_nonexistent_courier(self):
        with self.assertRaises(ValueError):
            self.board.remove_courier("nonexistent")

    def test_empty_board(self):
        self.assertEqual(self.board.get_orders(), [])
        self.assertEqual(self.board.get_couriers(), [])
        self.assertEqual(self.board.get_routes(), [])

if __name__ == '__main__':
    unittest.main()
