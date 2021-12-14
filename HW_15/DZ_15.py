from typing import Union


class Product:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f" {self.name} "

    def __repr__(self):
        return f" {self.name} "

    def get_total(self, units: Union[int, float]) -> float:
        return round(self.price * units, 2)


class Cart:
    def __init__(self):
        self.products = []
        self.units = []

    def __str__(self):
        return f"{len(self.products)} products."

    def __repr__(self):
        return f"{print(self.products, sep=', ')}"

    def add(self, product: Product, unit: Union[int, float]):
        self.products.append(product)
        self.units.append(unit)

    def total_cart(self):
        total_count = 0.0
        for product, unit in zip(self.products, self.units):
            total_count += product.get_total(unit)
            continue
        return f"full price been: {total_count} uah."


vodka = Product("grey_goose", 3)
grape = Product("kish-mish", 10)
cart = Cart()

cart.add(vodka, 5)
cart.add(grape, 8)




