from promocode import Promocode
from typing import List
from client import Client
from dataBase import SingletonMeta


class Admin(metaclass=SingletonMeta):

    @staticmethod
    def generate_promocode(percent: int) -> Promocode:
        return Promocode(percent)

    @staticmethod
    def send_promocode(clients: List[Client], promocode: Promocode) -> None:
        # рассылаем клиентам промокоды
        for client in clients:
            client.add_promo(promocode)
