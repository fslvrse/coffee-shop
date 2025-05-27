import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Coffee._all.clear()
        self.coffee = Coffee("Mocha")
        self.cust1 = Customer("Ali")
        self.cust2 = Customer("Zara")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_orders_and_customers(self):
        self.cust1.create_order(self.coffee, 5.0)
        self.cust2.create_order(self.coffee, 6.0)
        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertIn(self.cust1, self.coffee.customers())
        self.assertIn(self.cust2, self.coffee.customers())

    def test_num_orders_and_average_price(self):
        self.cust1.create_order(self.coffee, 4.0)
        self.cust2.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertEqual(self.coffee.average_price(), 5.0)
