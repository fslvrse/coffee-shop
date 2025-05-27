import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Customer._all.clear()
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")

    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 5.0)
        self.assertIsInstance(order, Order)

    def test_coffees(self):
        self.customer.create_order(self.coffee1, 5.0)
        self.customer.create_order(self.coffee2, 6.0)
        self.assertIn(self.coffee1, self.customer.coffees())
        self.assertIn(self.coffee2, self.customer.coffees())

    def test_most_aficionado(self):
        c2 = Customer("Charlie")
        self.customer.create_order(self.coffee1, 5.0)
        c2.create_order(self.coffee1, 6.0)
        self.assertEqual(Customer.most_aficionado(self.coffee1), c2)
