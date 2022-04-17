# Класс курьер
from enum import Enum


class Urgency(Enum):
    URGENT = 1  # URGENT delivery
    ASAP = 2  # as soon as possible, but not very urgent
    ONTIME = 3  # client chooses time


class Status(Enum):
    FREE = 1  # свободен, как ветер, можно юзать
    DELIVERING = 2  # доставляет
    RETURNSBACK = 3  # возвращается


class Courier:
    def __init__(self, name, surname, age, cnt_order):
        self.name = name
        self.surname = surname
        self.age = age
        self.urgency = Urgency.ASAP
        self.status = Status.FREE
        # how much orders
        self.cnt_order = cnt_order

    @property
    def name(self):
        return self.name

    @property
    def surname(self):
        return self.surname

    @property
    def age(self):
        return self.age

    @property
    def urgency(self):
        return self.urgency

    @property
    def status(self):
        return self.status

    @property
    def cnt_order(self):
        return self.cnt_order

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @surname.setter
    def surname(self, new_surname):
        self.surname = new_surname

    @age.setter
    def age(self, new_age):
        self.age = new_age

    @urgency.setter
    def urgency(self, new_urgency):
        self.urgency = new_urgency

    @status.setter
    def status(self, new_status):
        self.status = new_status

    @cnt_order.setter
    def cnt_order(self, new_cnt_order):
        self.cnt_order = new_cnt_order

    def check_workload(self):
        if (self.urgency == Urgency.ASAP or self.urgency == Urgency.ONTIME) \
           and self.cnt_order < 5:
            return True
        if self.urgency == Urgency.URGENT and self.cnt_order == 1:
            return True
        return False
