class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Invalid price')
        self.__price = price


product = Product(50)

print(product.price)

product.price = 10

print(product.price)
