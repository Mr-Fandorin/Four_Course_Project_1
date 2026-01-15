import pytest

from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products_list) == 3
    assert second_category.name == "Телевизоры"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products_property(first_category):
    assert first_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(first_category, product):
    assert len(first_category.products_list) == 3
    first_category.add_product(product)
    assert len(first_category.products_list) == 4


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_error(first_category, product):
    with pytest.raises(TypeError):
        first_category.add_product(1)

def test_middle_price(first_category, category_without_product):
    assert first_category.middle_price() == 140333.33333333334
    assert category_without_product.middle_price() == 0


