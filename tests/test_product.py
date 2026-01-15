import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 7


def test_new_product():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_price(product):
    product.price = -100
    assert product.price == 180000.0


def test_product_str(product):
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 7 шт."


def test_product_add(product, product_2):
    assert product + product_2 == 2940000.0

def test_product_init_2():
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
