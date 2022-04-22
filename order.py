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
    def __init__(self, order_id, promocode=None, product_list=[], payment=Payment.CARD):
        self.__order_id = order_id  # ID заказа
        self.__order_status = OrderStatus.NEW  # Статус заказа
        self.__product_list = product_list  # Список ProductShopAvaliability
        self.__starting_price = self.calculate_cost()  # Исходная цена заказа (без скидок)
        self.__payment = payment  # Способ оплаты
        self.__courier = None
        self.__promocode = promocode  # Промокод
        if self.promocode is not None:  # Цена со скидкой
            self.__total_price = self.apply_promocode()
        else:
            self.__total_price = self.starting_price

    # Геттеры
    @property
    def order_id(self):
        return self.__order_id

    @property
    def order_status(self):
        return self.__order_status

    @property
    def starting_price(self):
        return self.__starting_price

    @property
    def total_price(self):
        return self.__total_price

    @property
    def payment(self):
        return self.__payment

    @property
    def courier(self):
        return self.__courier

    @property
    def promocode(self):
        return self.__promocode

    @property
    def product_list(self):
        return self.__product_list

    # Сеттеры
    @order_status.setter
    def order_status(self, new_order_status):
        self.__order_status = new_order_status

    @starting_price.setter
    def starting_price(self, new_starting_price):
        self.__starting_price = new_starting_price

    @total_price.setter
    def total_price(self, new_total_price):
        self.__total_price = new_total_price

    @payment.setter
    def payment(self, new_payment):
        self.__payment = new_payment

    @courier.setter
    def courier(self, new_courier):
        self.__courier = new_courier

    @promocode.setter
    def promocode(self, new_promocode):
        self.__promocode = new_promocode

    def calculate_cost(self):
        result = 0
        for i in self.product_list:
            result += i.price
        return result

    def apply_promocode(self):
        al = self.starting_price
        return al + (al * self.promocode.precent / 100)
