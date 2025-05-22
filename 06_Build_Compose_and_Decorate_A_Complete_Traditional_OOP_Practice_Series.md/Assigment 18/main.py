class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Getter method to access the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter method to update the price."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter method to delete the price."""
        print("Deleting price...")
        del self._price
p = Product(100)
print(p.price)      # Output: 100

p.price = 150
print(p.price)      # Output: 150

del p.price         # Output: Deleting price...
