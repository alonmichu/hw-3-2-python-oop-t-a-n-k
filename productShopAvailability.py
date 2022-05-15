from product import Product
from shop import Shop
from decimal import Decimal


class ProductShopAvailability:  # Зависимость продукт - заказ
    def __init__(self, product_id, product: Product, shop: Shop, amount: int, price: Decimal):
        self.id = product_id
        self.product = product  # Продукт
        self.shop = shop  # Магазин
        self.amount = amount  # Количество продукта
        self.price = price  # Стоимость продукта

    def __str__(self):
        return f"{self.product},{self.shop}"
