from base import Base


class Shop(Base):

    def __init__(self, shop_name, shop_id):
        self._name = self.check_str(shop_name)
        self._id = shop_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.check_str(new_name)
        self._name = new_name

    def __str__(self):
        return f"{self._name}"
