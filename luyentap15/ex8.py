class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("price khong duoc < 0")
        self._price = price

p = Product(100)
print(p.get_price())

p.set_price(200)
print(p.get_price())