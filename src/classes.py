class Product:
    """Класс для представления продукта"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod):
        name = prod["name"]
        description = prod["description"]
        price = prod["price"]
        quantity = prod["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = val


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для представления категории"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."
