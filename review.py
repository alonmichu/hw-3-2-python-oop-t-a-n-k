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
        self._text = text
        self._star = star

    def edit(self) -> None:
        new_text = input("write edited text here: ")
        self._text = new_text

    def show(self):
        print(f"{self._star.value}\n {self._text}")

    @property
    def star(self):
        return self._star

    @property
    def text(self):
        return self._text
