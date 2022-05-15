import random

from order import Order
from productShopAvailability import ProductShopAvailability
from typing import List
from dataBase import PythonDb
from singleton import singleton


@singleton
class Collector:
    def __init__(self):
        pass

    def collect_order(self, order: Order, bd: PythonDb) -> None:
        total_list = []
        for p in order.product_list:
            collect_item = self.collect_item(p, bd)
            if collect_item is not None:
                total_list.append(collect_item)
        order.product_list = total_list
        order.calculate_cost()

    def collect_item(self, p: ProductShopAvailability, bd: PythonDb):
        p1 = bd.products.find(p.id)
        p1.amount = random.randrange(0, 100, 1)
        if p1.amount is not 0:
            return p1
        else:
            return None


    # def collect_item(self,p:ProductShopAvailability,product_list:List[ProductShopAvailability]):


c_a = Collector()
c_b = Collector()
print(c_a == c_b)
