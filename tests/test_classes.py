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
def category_2():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    ["product4", "product5", "product6"])


def test_init_category(category_2):
    assert category_2.name == "Телевизоры"
    assert category_2.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                      "станет вашим другом и помощником")
    assert category_2.products == ["product4", "product5", "product6"]
    assert category_2.category_count == 1
    assert category_2.product_count == 3
