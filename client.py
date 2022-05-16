import uuid

from base import Base
from order import Order, Payment
from product import Product
from productShopAvailability import ProductShopAvailability, ProductInOrder
from promocode import Promocode
from uuid import UUID
from typing import List, Union


class Client(Base):

    def __init__(self, client_id: UUID, name: str, surname: str, phone: str, mail: str,address:str):
        self.id = client_id
        self.name = self.check_str(name)
        self.surname = self.check_str(surname)
        self.address=address
        self.__phone = phone
        self._mail = mail
        self._cart_list: List[ProductInOrder] = []
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
    def cart_list(self, cart_elem: ProductInOrder):
        self._cart_list += [cart_elem]

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

    def add_to_cartlist(self, product: ProductShopAvailability, count: int) -> None:
        if self._cart_list:
            if product.shop != self._cart_list[0].shop or \
                    product.amount == 0:
                print(f"You can't add such product {product}")
            else:
                self._cart_list.append(ProductInOrder(product, count))
        else:
            self._cart_list.append(ProductInOrder(product, count))

    def del_from_cartlist(self, product: Union[ProductInOrder, ProductShopAvailability]) -> None:
        cart_dict = {prod.id: i for i, prod in enumerate(self._cart_list)}

        if product.id in cart_dict:
            del self._cart_list[cart_dict[product.id]]
        else:
            print(f'No such product in cart_list{product}')


    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self._mail}"
