from base import Base
from order import Order


class Client(Base):

    def __init__(self, name, surname, phone, mail):
        self._name = self.check_str(name)
        self._surname = self.check_str(surname)
        self.__phone = phone
        self._mail = mail
        self._cart_list = []
        self.__promo_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.check_str(new_name)
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self.check_str(new_surname)
        self._surname = new_surname

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def cart_list(self):
        return self._cart_list

    @cart_list.setter
    def mail(self, cart_elem):
        self._cart_list += [cart_elem.id]

    @property
    def promo_list(self):
        return self.__promo_list

    @promo_list.setter
    def mail(self, promo):
        self.__promo_list += [promo]

    # формирование отзыва
    def full_review(self, review):
        return f"{self._name} {self._surname}:" + review

    # добавление отзыва на конкретный продукт
    def add_review(self, product, review):
        product.review_list = self.full_review(review)

    def add_to_cartlist(self, p_sh_av):
        if self._cart_list != []:
            if p_sh_av.shop == self._cart_list[0].shop:
                self._cart_list.append(p_sh_av)
        self._cart_list.append(p_sh_av)

    def del_from_cartlist(self, p_sh_av):
        try:
            self._cart_list.remove(p_sh_av)
            raise ValueError
        except ValueError:
            print('No such element')

    # формируем заказ
    def checkout(self, payment, promocode=None):
        promo_avail = False
        if promocode is not None:
            promo_avail = promocode.available(self)
        if promo_avail is False:
            promocode = None
        order = Order(1, promocode, self._cart_list, payment)
        self._cart_list = []
        return order

    def __str__(self):
        return f"{self._name}\n{self._surname}\n{self.__mail}"
