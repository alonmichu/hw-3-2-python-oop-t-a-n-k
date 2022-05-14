from order import Order
from productShopAvailability import ProductShopAvailability
from typing import List


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Collector:
    def __init__(self):
        pass

    def collect_order(self, order: Order) -> None:
        for p in order.product_list:
            order.product_list = self.collect_item(p, order.product_list)

    # def collect_item(self,p:ProductShopAvailability,product_list:List[ProductShopAvailability]):


c_a = Collector()
c_b = Collector()
print(c_a == c_b)
