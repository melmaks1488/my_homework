from typing import Union,  Any


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
    products: list[Any]

    def __init__(self):
        self.products = []
        self.units = []

    def __str__(self):
        return f"{len(self.products)} products."

    def __repr__(self):
        return f"{print(*self.products)}"

    def add(self, product: Product, unit: Union[int, float]):
        self.products.append(product)
        self.units.append(unit)

    def total_cart(self):
        total = 0.0
        for product, unit in zip(self.products, self.units):
            total += product.get_total(unit)
            continue
        return f"all bean : {total} uah."

    def __add__(self, other):
        return print(*self.products + other.products)

    def __sub__(self, cart):
        return print(*set(self.products) - set(cart.products))


# Add products to our class "Product"
banana = Product("Banana", 15)
tomato = Product("Tomato", 14)
grape = Product("grape", 27)
beer = Product("Staropramen", 11)

print("We count the amount of products: ")
print("Banana cost: ", banana.get_total(2), "UAH.")
print("Tomato cost: ", tomato.get_total(5), "UAH.")
print("Grape cost: ", grape.get_total(4), "UAH.")
print("Staropramen cost: ", beer.get_total(5), "UAH.")

cart = Cart()  # create our cart # 1

# Add products to our cart
cart.add(banana, 2)
cart.add(grape, 4)
cart.add(tomato, 5)
cart.add(beer, 5)

cart2 = Cart()  # create our cart # 2

# Add products to our cart
cart2.add(banana, 1)
cart2.add(grape, 2)
cart2.add(tomato, 3)

# We calculate the cost of our basket of goods
print("All products price: ", cart.total_cart())

print(cart + cart2)
print(cart - cart2)