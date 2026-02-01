import pytest

from src.classes import Category, Product


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


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
                    [product1])


def test_init_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")
    assert category_1.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.']
    assert category_1.category_count == 1
    assert category_1.product_count == 1


def test_add_product(category_1: Category):
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert len(category_1.products) == 1
    category_1.add_product(product2)
    assert len(category_1.products) == 2

# def test_new_product