import pytest

from src.classes import Category, Product


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_init_product(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


@pytest.fixture
def category_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [product1, product2])


def test_init_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")
    assert category_1.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                   'Iphone 15, 210000.0 руб. Остаток: 8 шт.']
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_add_product(category_1: Category):
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert len(category_1.products) == 2
    category_1.add_product(product3)
    assert len(category_1.products) == 3


def test_new_product():
    new_prod = Product.new_product({"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0,
                                    "quantity": 7})
    assert new_prod.name == "55\" QLED 4K"
    assert new_prod.description == "Фоновая подсветка"
    assert new_prod.price == 123000.0
    assert new_prod.quantity == 7


def test_price():
    new_prod_2 = Product.new_product({"name": "Nokia", "description": "Экран", "price": 90.0, "quantity": 7})
    assert new_prod_2.price == 90.0
    new_prod_2.price = -75.0
    assert new_prod_2.price == 90.0
    new_prod_2.price = 0.0
    assert new_prod_2.price == 90.0
