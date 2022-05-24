from typing import List
from review import Review, Star_mark
from uuid import UUID


class Product:

    def __init__(self, product_id: UUID, product_name: str, description: str = None):
        self.id = product_id
        self.name = product_name
        if description is not None:
            self.description = description
        self._review_list = []

    @property
    def review_list(self):
        return self._review_list

    @review_list.setter
    def review_list(self, review: List[str]):
        self._review_list = review

    def add_review(self, new_review: str) -> None:
        self.review_list += [new_review]

    def see_review(self):
        for i in range(len(self.review_list)):
            print(self.review_list[i])

    def __str__(self):
        return f"{self.name}:{self.description}"
