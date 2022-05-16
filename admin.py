from promocode import Promocode
from typing import List
from client import Client


# Класс администроатора

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Admin:
    def __init__(self):
        pass

    @staticmethod
    def generate_promocode(percent: int) -> Promocode:
        return Promocode(percent)

    @staticmethod
    def send_promocode(clients: List[Client], promocode: Promocode):
        for client in clients:
            client.promo_list = promocode
