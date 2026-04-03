class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # getter name
    def get_name(self):
        return self._name

    # setter name
    def set_name(self, name):
        self._name = name

    # getter price
    def get_price(self):
        return self._price

    # setter price
    def set_price(self, price):
        self._price = price


# Khởi tạo đối tượng
b1 = Book("Python Basic", 150)

# In ra giá trị price
print("Price:", b1.get_price())