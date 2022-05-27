from enum import Enum
from courier import Urgency
from uuid import UUID
from promocode import Promocode
from typing import List
from productShopAvailability import ProductInOrder
from decimal import Decimal
from datetime import datetime


class OrderStatus(Enum):  # Статусы заказа
    NEW = 1
    ASSEMBLY = 2
    READY_FOR_DELIVERY = 3
    DELIVERED = 4


class Payment(Enum):  # Способы оплаты
    CASH = 1
    CARD = 2


class Order:  # Заказ
    def __init__(self, order_id: UUID, address: str, product_list: List[ProductInOrder],
                 promocode: Promocode = None,
                 payment: Payment = Payment.CARD, urgency: Urgency = Urgency.ASAP):
        self.id = order_id
        self.address = address
        self.order_status: OrderStatus = OrderStatus.NEW
        self.product_list: List[ProductInOrder] = product_list
        self.starting_price = self.calculate_cost()  # Исходная цена заказа (без скидок)
        self.payment = payment
        self.courier = None
        self.promocode = promocode
        self.urgency = urgency
        self.date_create = datetime.now()
        if self.promocode is not None:
            self.total_price = self.apply_promocode()
        else:
            self.total_price = self._starting_price

    def apply_promocode(self) -> Decimal:
        sale = Decimal(1 - self.promocode.percent / 100) * Decimal(1.00)
        res = sale * self.starting_price
        return res.quantize(Decimal('.01'))

    def calculate_cost(self) -> Decimal:
        res = Decimal(0)
        for product in self.product_list:
            res += product.price * product.cnt
        return res.quantize(Decimal('.01'))

    def __str__(self):
        d = {prod.product.name: prod.cnt for prod in self.product_list}
        return f"{d}:{self.order_status}\n" \
               f"starting price:{self.starting_price}\n" \
               f"total price:{self.total_price}\n" \
               f"courier:{self.courier}\n" \
               f"date:{self.date_create}"
