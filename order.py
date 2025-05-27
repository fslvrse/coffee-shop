class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer.add_order(self)
        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, "_price"):
            raise AttributeError("Price cannot be changed after initialization.")
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
