class ProductShopAvailability:  # Зависимость продукт - заказ
    def __init__(self, product, shop, amount, price):
        self._product = product  # Продукт
        self._shop = shop  # Магазин
        self._amount = amount  # Количество продукта
        self._price = price  # Стоимость продукта

    # Геттеры
    @property
    def product(self):
        return self._product

    @property
    def shop(self):
        return self._shop

    @property
    def amount(self):
        return self._amount

    @property
    def price(self):
        return self._price

    # Сеттеры
    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @price.setter
    def price(self, new_price):
        self._price = new_price
