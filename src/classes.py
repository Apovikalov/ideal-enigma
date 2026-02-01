class Product:
    """Класс для представления продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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
        self.__products.append(product)

    @property
    def products(self):
        list_of_prod = []
        for i in self.__products:
             list_of_prod.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return list_of_prod
