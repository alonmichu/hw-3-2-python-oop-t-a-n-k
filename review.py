# Класс отзывов на продукты
from enum import Enum


class Star_mark(Enum):
    FAIL = 1
    BAD = 2
    SATISFACTORY = 3
    GOOD = 4
    EXCELLENT = 5


class Review:
    def __init__(self, text: str, star: Star_mark):
        self.text = text
        self.star = star

    def edit(self) -> None:
        new_text = input("write edited text here: ")
        self.text = new_text

    def show(self):
        print(f"{self.star.value}\n {self.text}")


