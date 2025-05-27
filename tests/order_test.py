import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jane")
        self.coffee = Coffee("Americano")

    def test_valid_order(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_customer(self):
        with self.assertRaises(ValueError):
            Order("not_customer", self.coffee, 5.0)

    def test_invalid_coffee(self):
        with self.assertRaises(ValueError):
            Order(self.customer, "not_coffee", 5.0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "cheap")
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 15.0)
