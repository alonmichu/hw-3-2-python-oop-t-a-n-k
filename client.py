from product import Product
from productShopAvailability import ProductShopAvailability, ProductInOrder
from promocode import Promocode
from uuid import UUID
from typing import List, Union
from review import Review
from review import Star_mark


class Client:

    def __init__(self, client_id: UUID, name: str, surname: str,
                 address: str, mail: str, phone: str):
        self.id = client_id
        self.name = name
        self.surname = surname
        self.address = address
        self.mail = mail
        self.phone = phone
        self.cart_list: List[ProductInOrder] = []
        self.promo_list: List[Promocode] = []

    # добавление отзыва на конкретный продукт
    def write_review(self, product: Product,
                     mark_star: Star_mark, review_text: str) -> None:
        review = Review(name=self.name, surname=self.surname,
                        text=review_text, star=mark_star)
        product.add_review(review)

    def add_to_cartlist(self, product: ProductShopAvailability,
                        count: int) -> None:
        if self.cart_list:
            if product.shop != self.cart_list[0].shop or \
                    product.amount == 0:
                raise TypeError(f"You can't add such product {product}")
            else:
                self.cart_list.append(ProductInOrder(product, count))
        else:
            self.cart_list.append(ProductInOrder(product, count))

    def del_from_cartlist(self,
                          product: Union[ProductInOrder,
                                         ProductShopAvailability]) -> None:
        index = -1
        for idx, prod in enumerate(self.cart_list):
            if product.id == prod.id:
                index = idx
        if index != -1:
            del self.cart_list[index]
        else:
            raise IndexError(f"No such product in cart_list {product}")

    def clean_cart_list(self) -> None:
        self.cart_list = []

    def add_promo(self, promo: Promocode) -> None:
        self.promo_list += [promo]

    def del_from_promolist(self, promocode: Promocode) -> None:
        index = -1
        for idx, promo in enumerate(self.promo_list):
            if promocode.promocode_id == promo.promocode_id:
                index = idx
        if index != -1:
            del self.promo_list[index]
        else:
            raise IndexError(f"No such promo in promo_list {promocode}")

    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self.mail}"
