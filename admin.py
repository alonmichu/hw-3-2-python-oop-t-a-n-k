from promocode import Promocode
from typing import List
from client import Client
from dataBase import SingletonMeta


class Admin(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def generate_promocode(percent: int) -> Promocode:
        return Promocode(percent)

    @staticmethod
    def send_promocode(clients: List[Client], promocode: Promocode):
        for client in clients:
            client.promo_list = promocode
