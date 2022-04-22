# Класс курьер
from enum import Enum
from base import Base


class Urgency(Enum):
    URGENT = 1  # URGENT delivery
    ASAP = 2  # as soon as possible, but not very urgent
    ONTIME = 3  # client chooses time


class CourierStatus(Enum):
    FREE = 1  # свободен, как ветер, можно юзать
    DELIVERING = 2  # доставляет
    RETURNSBACK = 3  # возвращается


class Courier(Base):
    def __init__(self, name, surname, age, cnt_order):
        self._name = self.check_str(name)
        self._surname = self.check_str(surname)
        self._age = age
        self._urgency = Urgency.ASAP
        self._status = CourierStatus.FREE
        # how many orders
        self._cnt_order = cnt_order

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def urgency(self):
        return self._urgency

    @property
    def status(self):
        return self._status

    @property
    def cnt_order(self):
        return self._cnt_order

    @name.setter
    def name(self, new_name):
        self._name = self.check_str(new_name)

    @surname.setter
    def surname(self, new_surname):
        self._surname = self.check_str(new_surname)

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @urgency.setter
    def urgency(self, new_urgency):
        self._urgency = new_urgency

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @cnt_order.setter
    def cnt_order(self, new_cnt_order):
        self._cnt_order = new_cnt_order

    def check_workload(self):
        if (self._urgency == Urgency.ASAP
            or self._urgency == Urgency.ONTIME) \
                and self._cnt_order < 5:
            return True
        if self._urgency == Urgency.URGENT and self._cnt_order == 1:
            return True
        return False

    def check_status(self):
        print("Now my status is: "+str(self._status))

    def __str__(self):
        return f"Hello!I am {self._name} " \
               f"{self._surname} {self._age} y.o."