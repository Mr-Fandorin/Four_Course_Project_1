import pytest


def test_lawngrass_product_init(lawngrass_product):
    assert lawngrass_product.name == "Газонная трава"
    assert lawngrass_product.description == "Элитная трава для газона"
    assert lawngrass_product.price == 500.0
    assert lawngrass_product.quantity == 20
    assert lawngrass_product.country == "Россия"
    assert lawngrass_product.germination_period == "7 дней"
    assert lawngrass_product.color == "Зеленый"

def test_lawngrass_product_add(lawngrass_product, lawngrass_product_2):
    assert lawngrass_product + lawngrass_product_2 == 16750

def test_lawngrass_product_error(lawngrass_product):
    with pytest.raises(TypeError):
        result = lawngrass_product + 1