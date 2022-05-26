from enum import Enum
from uuid import UUID


class Urgency(Enum):
    URGENT = 1  # URGENT delivery
    ASAP = 2  # as soon as possible, but not very urgent


class CourierStatus(Enum):
    FREE = 1  # свободен, как ветер, можно юзать
    DELIVERING = 2  # доставляет
    DAY_OFF = 3  # не боспокойте, у него выходной


class Courier:
    def __init__(self, courier_id: UUID, name: str, surname: str,
                 age: int, urgency: Urgency):
        self.id = courier_id
        self.name = name
        self.surname = surname
        self.age = age
        self.urgency = urgency
        self.status: CourierStatus = CourierStatus.FREE

    def check_status(self) -> str:
        return f"Now {self.name} {self.surname} status is: " \
               + str(self.status)

    def __str__(self):
        return f"{self.name} " \
               f"{self.surname} {self.age} y.o."
