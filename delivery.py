# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
import uuid
from typing import Union
from courier import Courier, CourierStatus
from client import Client
from order import Payment
from product import Product
from admin import Admin
from order import Order, OrderStatus
from promocode import Promocode
from dataBase import PythonDb
from productShopAvailability import ProductInOrder
from random import choice

DB = PythonDb()


# формируем заказ
def checkout(client: Client, payment: Payment, promocode: Promocode = None) -> Order:
    if promocode is not None:
        if promocode.available(client.id) is False \
                or promocode not in client.promo_list:
            promocode = None
        else:
            promocode.add_user_who_used(client.id)

    order = DB.create_order(address=client.address, client_obj=client, payment=payment, promocode=promocode)
    client.cart_list = []
    return order


def collect_item(p: ProductInOrder) -> Union[None, ProductInOrder]:
    if not isinstance(p,ProductInOrder):
        return None
    p1 = DB.products.find(p.id)
    if p1.amount > 0 and p1.amount >= p.cnt:
        p1.amount -= p.cnt
        return ProductInOrder(p1, p.cnt)
    else:
        return None


def collect_order(order: Order) -> None:
    total_list = []
    for p in order.product_list:
        collected_item = collect_item(p)
        if collected_item is not None:
            total_list.append(collected_item)
    order.product_list = total_list
    order.calculate_cost()
    order.order_status = OrderStatus.ASSEMBLY


def get_in_delivery(order: Order):
    order.courier = choice(DB.get_free_couriers(order.urgency))
    order.courier.status = CourierStatus.DELIVERING
    order.order_status = OrderStatus.SENT


def finish_order(order: Order):
    order.courier.status = CourierStatus.FREE
    order.order_status = OrderStatus.DELIVERED


if __name__ == '__main__':
    shop_1 = DB.create_shop('Vkusvill')
    shop_2 = DB.create_shop('Magnit')
    shop_3 = DB.create_shop('Lenta')
    p_1 = Product('apple', 'green apple')
    p_2 = Product('apple', 'red apple')
    p_3 = Product('chocolate', 'bitter chocolate 100g')
    p_4 = Product('bananas', '-')
    p_5 = Product('manga', 'yellow sweet manga')

    p_sh_a_1 = DB.create_product(p_1, shop_1, 12, 23.20)
    p_sh_a_2 = DB.create_product(p_1, shop_2, 3, 24.00)
    p_sh_a_3 = DB.create_product(p_2, shop_2, 5, 25.50)
    p_sh_a_4 = DB.create_product(p_3, shop_3, 8, 105)
    p_sh_a_5 = DB.create_product(p_4, shop_3, 25, 15.35)
    p_sh_a_6 = DB.create_product(p_5, shop_3, 4, 180.50)
    p_sh_a_7 = DB.create_product(p_5, shop_2, 2, 155.60)

    client_1 = DB.create_client('Vanya', 'Petrov', '987539487', 'Petr234@mail.ru', 'Ukhtomskogo 21')
    client_2 = DB.create_client('Petr', 'Ivanov', '987534112', 'Ivan1@mail.ru', 'Uglicheskay 5')
    client_2.add_to_cartlist(p_sh_a_3, 2)
    client_1.add_to_cartlist(p_sh_a_6, 3)
    client_1.add_to_cartlist(p_sh_a_5, 1)
    client_1.add_to_cartlist(p_sh_a_4, 2)
    client_1.add_to_cartlist(p_sh_a_2, 3)
    client_1.del_from_cartlist(p_sh_a_1)
    client_1.del_from_cartlist(p_sh_a_5)

    admin = Admin()
    new_promo1 = admin.generate_promocode(10)
    admin.send_promocode([client_1], new_promo1)
    new_promo2 = admin.generate_promocode(5)
    admin.send_promocode([client_1, client_2], new_promo2)

    order_1 = DB.create_from_obj(checkout(client=client_1, payment=Payment.CASH,
                                          promocode=new_promo2))
    print(order_1)
    order_2 = DB.create_from_obj(checkout(client=client_2, payment=Payment.CARD,
                                          promocode=new_promo1))
    print(order_2)

    courier = DB.create_courier("Stepan", "Musorskiy", 34, 0)
    print(courier)

    collect_order(order_1)
    get_in_delivery(order_1)
    finish_order(order_1)
    collect_order(order_2)
    get_in_delivery(order_2)
    finish_order(order_2)
