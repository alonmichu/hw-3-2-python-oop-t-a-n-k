from typing import List
from uuid import UUID
from review import Review


class Product:

    def __init__(self, product_id: UUID, product_name: str,
                 description: str = None):
        self.id = product_id
        self.name = product_name
        if description is not None:
            self.description = description
        self.review_list: List[Review] = []

    def add_review(self, new_review: Review) -> None:
        self.review_list += [new_review]

    def see_review(self) -> None:
        print(f"Review for {self.name}")
        for i in range(len(self.review_list)):
            self.review_list[i].show()

    def __str__(self):
        return f"{self.name}:{self.description}"
