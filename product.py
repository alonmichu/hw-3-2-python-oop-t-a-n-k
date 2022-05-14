from base import Base


class Product(Base):

    def __init__(self, product_name: str, description: str = None):
        self.name = self.check_str(product_name)
        if description is not None:
            self.description = description
        self._review_list = []

    @property
    def review_list(self):
        return self._review_list

    @review_list.setter
    def review_list(self, review: str):
        self._review_list += [review]

    def __str__(self):
        return f"{self.name}:{self.description}"
