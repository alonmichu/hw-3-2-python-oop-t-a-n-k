from enum import Enum
from courier import Urgency
from uuid import uuid4, UUID
from promocode import Promocode
from typing import List
from productShopAvailability import ProductShopAvailability
from decimal import Decimal
from courier import Courier
from datetime import datetime


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
    def __init__(self, product_list: List[ProductShopAvailability], promocode: Promocode = None,
                 payment: Payment = Payment.CARD, urgency: Urgency = Urgency.ASAP):
        self.id: UUID = uuid4()
        self._order_status: OrderStatus = OrderStatus.NEW
        self._product_list = product_list
        self._starting_price = self.calculate_cost()  # Исходная цена заказа (без скидок)
        self._payment = payment
        self._courier = None
        self._promocode = promocode
        self._urgency = urgency
        self._date_create = datetime.now()
        if self.promocode is not None:
            self._total_price = self.apply_promocode()
        else:
            self._total_price = self._starting_price

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

    @property
    def urgency(self):
        return self._urgency

    # Сеттеры
    @order_status.setter
    def order_status(self, new_order_status: OrderStatus):
        self._order_status = new_order_status

    @starting_price.setter
    def starting_price(self, new_starting_price: Decimal):
        self._starting_price = new_starting_price

    @total_price.setter
    def total_price(self, new_total_price: Decimal):
        self._total_price = new_total_price

    @payment.setter
    def payment(self, new_payment: Payment):
        self._payment = new_payment

    @courier.setter
    def courier(self, new_courier: Courier):
        self._courier = new_courier

    @promocode.setter
    def promocode(self, new_promocode: Promocode):
        self._promocode = new_promocode

    @urgency.setter
    def urgency(self, new_urgency: Urgency):
        self._urgency = new_urgency

    def calculate_cost(self) -> Decimal:
        res = Decimal(0)
        for i in self.product_list:
            res += i.price
        return res.quantize(Decimal('.01'))

    def apply_promocode(self) -> Decimal:
        sale = Decimal(1 - self.promocode.percent / 100) * Decimal(1.00)
        res = sale * self._starting_price
        return res.quantize(Decimal('.01'))

    def __str__(self):
        return f"{self._product_list}:{self._order_status}\n" \
               f"starting price:{self._starting_price}\n" \
               f"total price:{self._total_price}"
