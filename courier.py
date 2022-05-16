from enum import Enum
from uuid import UUID


class Urgency(Enum):
    URGENT = 1  # URGENT delivery
    ASAP = 2  # as soon as possible, but not very urgent


class CourierStatus(Enum):
    FREE = 1  # свободен, как ветер, можно юзать
    DELIVERING = 2  # доставляет


class Courier:
    def __init__(self, courier_id: UUID, name: str, surname: str,
                 age: int, urgency: Urgency):
        self.id = courier_id
        self.name = name
        self.surname = surname
        self._age = age
        self._urgency = urgency
        self._status: CourierStatus = CourierStatus.FREE

    @property
    def age(self):
        return self._age

    @property
    def urgency(self):
        return self._urgency

    @property
    def status(self):
        return self._status

    @age.setter
    def age(self, new_age: int):
        self._age = new_age

    @urgency.setter
    def urgency(self, new_urgency: Urgency):
        self._urgency = new_urgency

    @status.setter
    def status(self, new_status: CourierStatus):
        self._status = new_status

    def check_status(self) -> str:
        return f"Now {self.name} {self.surname} status is: "\
               + str(self._status)

    def __str__(self):
        return f"{self.name} " \
               f"{self.surname} {self._age} y.o."
