from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            print("Товар с нулевым количеством не может быть добавлен")
            raise ValueError


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

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


class MixinLog:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    def __repr__(self):
        return f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, MixinLog):
    """Класс для представления продукта"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """Смартфоны"""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Трава газонная"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для представления категории"""
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        mid_price = 0
        try:
            for i in self.__products:
                mid_price += i.price
            mid_price /= len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return mid_price

    @property
    def products(self):
        list_of_prod = []
        for i in self.__products:
            list_of_prod.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return list_of_prod

    @property
    def quant_count(self):
        all_prods_quant = 0
        for i in self.__products:
            all_prods_quant += i.quantity
        return all_prods_quant

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.quant_count} шт."
