from base import Base
from order import Order
# from dataBase import add_orders, orders_base


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
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, new_mail):
        self._mail = new_mail

    @property
    def cart_list(self):
        return self._cart_list

    @cart_list.setter
    def cart_list(self, cart_elem):
        self._cart_list += [cart_elem.id]

    @property
    def promo_list(self):
        return self.__promo_list

    @promo_list.setter
    def promo_list(self, promo):
        self.__promo_list += [promo]

    # формирование отзыва
    def full_review(self, review):
        return f"{self._name} {self._surname}:" + review

    # добавление отзыва на конкретный продукт
    def add_review(self, product, review):
        product.review_list = self.full_review(review)

    def add_to_cartlist(self, p_sh_av):
        if self._cart_list:
            if p_sh_av.shop != self._cart_list[0].shop or \
                    p_sh_av.amount == 0:
                print(f"You can't add such product {p_sh_av}")
            else:
                self._cart_list.append(p_sh_av)
        else:
            self._cart_list.append(p_sh_av)

    def del_from_cartlist(self, p_sh_av):
        try:
            self._cart_list.remove(p_sh_av)
            raise ValueError
        except ValueError:
            print(f'No such element {p_sh_av}')

    # формируем заказ
    def checkout(self, payment, promocode=None):
        if promocode is not None:
            if promocode.available(self) is False:
                promocode = None
        order = Order(promocode, self._cart_list, payment)
        #add_orders(order)
        self._cart_list = []
        return order

    def __str__(self):
        return f"{self._name}\n{self._surname}\n{self._mail}"
