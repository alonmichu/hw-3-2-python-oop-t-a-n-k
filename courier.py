# Класс курьер
from enum import Enum
from base import Base
from uuid import UUID, uuid4


class Urgency(Enum):
    URGENT = 1  # URGENT delivery
    ASAP = 2  # as soon as possible, but not very urgent
    ONTIME = 3  # client chooses time


class CourierStatus(Enum):
    FREE = 1  # свободен, как ветер, можно юзать
    DELIVERING = 2  # доставляет
    RETURNSBACK = 3  # возвращается


class Courier(Base):
    def __init__(self, name: str, surname: str, age: int, cnt_order: int):
        self.id: UUID = uuid4()
        self.name = self.check_str(name)
        self.surname = self.check_str(surname)
        self._age = age
        self._urgency: Urgency = Urgency.ASAP
        self._status: CourierStatus = CourierStatus.FREE
        # how many orders
        self._cnt_order = cnt_order

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

    @age.setter
    def age(self, new_age: int):
        self._age = new_age

    @urgency.setter
    def urgency(self, new_urgency: Urgency):
        self._urgency = new_urgency

    @status.setter
    def status(self, new_status: CourierStatus):
        self._status = new_status

    @cnt_order.setter
    def cnt_order(self, new_cnt_order: int):
        self._cnt_order = new_cnt_order

    def check_workload(self) -> bool:
        if (self._urgency == Urgency.ASAP
            or self._urgency == Urgency.ONTIME) \
                and self._cnt_order < 5:
            return True
        if self._urgency == Urgency.URGENT and self._cnt_order == 1:
            return True
        return False

    def check_status(self) -> str:
        return "Now my status is: " + str(self._status)

    def __str__(self):
        return f"Hello!I am {self.name} " \
               f"{self.surname} {self._age} y.o."
