from enum import Enum


class OrderStatus(Enum):  # Статусы заказа
    NEW = 1
    ASSEMBLY = 2
    SENT = 3
    DELIVERED = 4
    CANCELED = 5


class Payment(Enum):  # Способы оплаты
    CASH = 1
    CARD = 2


class Order:  # Заказ
    def __init__(self, promocode=None, product_list=[], payment=Payment.CARD):
        self._order_status = OrderStatus.NEW  # Статус заказа
        self._product_list = product_list  # Список ProductShopAvaliability
        self._starting_price = self.calculate_cost()  # Исходная цена заказа (без скидок)
        self._payment = payment  # Способ оплаты
        self._courier = None
        self._promocode = promocode  # Промокод
        if self.promocode is not None:  # Цена со скидкой
            self._total_price = self.apply_promocode()
        else:
            self._total_price = self.starting_price

    # Геттеры
    @property
    def order_status(self):
        return self._order_status

    @property
    def starting_price(self):
        return self._starting_price

    @property
    def total_price(self):
        return self._total_price

    @property
    def payment(self):
        return self._payment

    @property
    def courier(self):
        return self._courier

    @property
    def promocode(self):
        return self._promocode

    @property
    def product_list(self):
        return self._product_list

    # Сеттеры
    @order_status.setter
    def order_status(self, new_order_status):
        self._order_status = new_order_status

    @starting_price.setter
    def starting_price(self, new_starting_price):
        self._starting_price = new_starting_price

    @total_price.setter
    def total_price(self, new_total_price):
        self._total_price = new_total_price

    @payment.setter
    def payment(self, new_payment):
        self._payment = new_payment

    @courier.setter
    def courier(self, new_courier):
        self._courier = new_courier

    @promocode.setter
    def promocode(self, new_promocode):
        self._promocode = new_promocode

    def calculate_cost(self):
        result = 0
        for i in self.product_list:
            result += i.price
        return result

    def apply_promocode(self):
        al = self.starting_price
        return al + (al * self.promocode.precent / 100)
