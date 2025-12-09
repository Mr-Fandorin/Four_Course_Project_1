from src.product import Product


class Category:
    """Класс категории продуктов"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        all_quantity_in_category = 0
        for product in self.__products:
            all_quantity_in_category += product.quantity
        return f"{self.name}, количество продуктов: {all_quantity_in_category} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_list(self):
        return self.__products
