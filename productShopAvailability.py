from product import Product
from decimal import Decimal
from uuid import UUID


class ProductShopAvailability:  # Зависимость продукт - заказ
    def __init__(self, product_id: UUID, product: Product, shop: UUID, amount: int, price: Decimal):
        self.id = product_id
        self.product = product  # Продукт
        self.shop = shop  # Магазин
        self.amount = amount  # Количество продукта
        self.price = price  # Стоимость продукта

    def __str__(self):
        return f"{self.product},{self.amount}"


class ProductInOrder(object):
    def __init__(self, product: ProductShopAvailability, count: int):
        self.id = product.id
        self.product_name = product.product.name
        self.shop = product.shop
        self.amount = product.amount
        self.price = product.price
        self.cnt = count

    def __str__(self):
        return f"{self.product_name},{self.cnt}"
