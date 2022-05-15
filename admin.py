from promocode import Promocode
from typing import List
from client import Client
from singleton import singleton

# Класс администроатора


@singleton
class Admin:
    def __init__(self):
        pass

    @staticmethod
    def generate_promocode(percent: int) -> Promocode:
        return Promocode([], percent)

    @staticmethod
    def send_promocode(clients: List[Client], promocode: Promocode):
        for client in clients:
            client.promo_list = promocode


"""
c_a = Admin()
c_b = Admin()
print(c_a == c_b)
client1 = Client("Ali", "Michu", "+79038210575", "meow.mail")
"""
# promo1 = c_a.generate_promocode("000001", "15")
# print(f"{promo1.promocode_id()} for {promo1.percent()}% discount")
# c_a.send_promocode(client1, promo1)
# print(f"client {client1.name} {client1.surname} has promos:")
# promo = client1.promo_list()[0]
# print(f"{promo.promocode_id()} for {promo.percent()}% discount")
