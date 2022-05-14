from product import Product
from shop import Shop
from decimal import Decimal
from uuid import uuid4, UUID


class ProductShopAvailability:  # Зависимость продукт - заказ
    def __init__(self, product: Product, shop: Shop, amount: int, price: Decimal):
        self.id: UUID = uuid4()
        self.product = product  # Продукт
        self.shop = shop  # Магазин
        self.amount = amount  # Количество продукта
        self.price = price  # Стоимость продукта

    def __str__(self):
        return f"{self.product},{self.shop}"
