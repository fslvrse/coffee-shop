class Coffee:
    def __init__(self, name):
        self.name = name  # Uses setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Coffee name cannot be changed after initialization.")
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def orders(self):
        return self._orders.copy()

    def customers(self):
        return list({order.customer for order in self._orders})

    def add_order(self, order):
        self._orders.append(order)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
