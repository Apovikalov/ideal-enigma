import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def smartphone_1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
                      95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      98.2, "15", 512, "Gray space")


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_0():
    with pytest.raises(ValueError):
        return Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_init_smartphone(smartphone_1):
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_init_grass(grass_1):
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_repr_product(smartphone_1, smartphone_2):
    assert repr(smartphone_1) == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    assert repr(smartphone_2) == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_str_product(smartphone_1, smartphone_2):
    assert str(smartphone_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(smartphone_2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 2580000


def test_add_type_error(smartphone_1, grass_1):
    with pytest.raises(TypeError):
        test_add(smartphone_1, grass_1)


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


def test_str_category(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 13 шт."


def test_add_product(category_1: Category):
    product3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                          90.3, "Note 11", 1024, "Синий")
    assert len(category_1.products) == 2
    category_1.add_product(product3)
    assert len(category_1.products) == 3


def test_add_product_type_error(category_1):
    with pytest.raises(TypeError):
        test_add_product(category_1, "Not a product")


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
