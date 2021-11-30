class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_total(self, pcs):
        p = self.price * pcs
        return p

class Product_cart:
        def __init__(self):
            self.c = list()
        def add(self, product, pcs):
            self.c.append(product.price * pcs)

        def get_total(self):
            k = sum(self.c)
            return k

apple = Product("apple", 10)
banana = Product("banana", 15)
cart = Product_cart()







