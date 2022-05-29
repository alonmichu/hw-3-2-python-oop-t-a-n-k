# Класс отзывов на продукты
from enum import Enum


class Star_mark(Enum):
    FAIL = 1
    BAD = 2
    SATISFACTORY = 3
    GOOD = 4
    EXCELLENT = 5


class Review:
    def __init__(self, name: str, surname: str, text: str, star: Star_mark):
        self.client_name = name
        self.client_surname = surname
        self.text = text
        self.star = star

    def edit(self, new_text: str) -> None:
        self.text = new_text

    def full_review_text(self) -> str:
        review = self.client_name + " " + self.client_surname + ":\n" + "⧫" * \
                 self.star.value + "◊" * (5 - self.star.value) + \
                 "\n" + self.text + "\n"
        return review
