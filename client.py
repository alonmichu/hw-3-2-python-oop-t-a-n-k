from base import Base
from order import Order, Payment
from product import Product
from productShopAvailability import ProductShopAvailability
from promocode import Promocode
from uuid import uuid4, UUID
from typing import List


class Client(Base):

    def __init__(self, name: str, surname: str, phone: str, mail: str):
        self.id: UUID = uuid4()
        self.name = self.check_str(name)
        self.surname = self.check_str(surname)
        self.__phone = phone
        self._mail = mail
        self._cart_list: List[ProductShopAvailability] = []
        self._promo_list: List[Promocode] = []

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone: str):
        self.__phone = new_phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, new_mail: str):
        self._mail = new_mail

    @property
    def cart_list(self):
        return self._cart_list

    @cart_list.setter
    def cart_list(self, cart_elem: ProductShopAvailability):
        self._cart_list += [cart_elem.id]

    @property
    def promo_list(self):
        return self._promo_list

    @promo_list.setter
    def promo_list(self, promo: Promocode):
        self._promo_list += [promo]

    # формирование отзыва
    def full_review(self, review: str) -> str:
        return f"{self.name} {self.surname}:" + review

    # добавление отзыва на конкретный продукт
    def add_review(self, product: Product, review: str) -> None:
        product.review_list = self.full_review(review)

    def add_to_cartlist(self, product_shop_availability: ProductShopAvailability) -> None:
        if self._cart_list:
            if product_shop_availability.shop != self._cart_list[0].shop or \
                    product_shop_availability.amount == 0:
                print(f"You can't add such product {product_shop_availability}")
            else:
                self._cart_list.append(product_shop_availability)
        else:
            self._cart_list.append(product_shop_availability)

    def del_from_cartlist(self, product_shop_availability: ProductShopAvailability) -> None:
        if product_shop_availability in self._cart_list:
            self._cart_list.remove(product_shop_availability)
        else:
            print(f'No such product in cart_list{product_shop_availability}')

    # формируем заказ
    def checkout(self, payment: Payment, promocode: Promocode = None) -> Order:
        if promocode is not None:
            if promocode.available(self.id) is False\
                    or promocode not in self._promo_list:
                promocode = None
            else:
                promocode.add_user_who_used(self.id)
        order = Order(self._cart_list, promocode, payment)
        self._cart_list = []
        return order

    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self._mail}"
