from base import Base


class Product(Base):

    def __init__(self, product_name, product_id, description=''):
        self._name = self.check_str(product_name)
        self._id = product_id
        self._description = description
        self._review_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.check_str(new_name)
        self._name = new_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def review_list(self):
        return self._review_list

    @review_list.setter
    def review_list(self, review):
        self._review_list += [review]

    def __str__(self):
        return f"{self._name}:\n{self._description}"
