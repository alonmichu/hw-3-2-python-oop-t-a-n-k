# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
from typing import Union
from courier import CourierStatus, Urgency
from client import Client
from order import Payment
from admin import Admin
from order import Order, OrderStatus
from promocode import Promocode
from dataBase import PythonDb
from productShopAvailability import ProductInOrder
from random import choice
from review import Star_mark

DB = PythonDb()


# формируем заказ
def checkout(client: Client, payment: Payment, address: str,
             promocode: Promocode = None, urgency: Urgency = Urgency.ASAP) -> Order:
    if promocode is not None:
        if promocode.available(client.id) is False \
                or promocode not in client.promo_list:
            promocode = None
        else:
            promocode.add_user_who_used(client.id)

    order = DB.create_order(address=address, client_obj=client,
                            payment=payment, promocode=promocode, urgency=urgency)
    client.clean_cart_list()
    return order


def collect_item(product: ProductInOrder) -> Union[None, ProductInOrder]:
    product1 = DB.products.find(product.id)
    if product1 is not None:
        if product1.amount > 0:
            if product1.amount >= product.cnt:
                product1.amount -= product.cnt
            else:
                product.cnt = product1.amount
                product1.amount = 0
            return product
    return None


def collect_order(order: Order) -> None:
    total_list = []
    for p in order.product_list:
        collected_item = collect_item(p)
        if collected_item is not None:
            total_list.append(collected_item)
    order.product_list = total_list
    order.starting_price = order.calculate_cost()
    if order.promocode is not None:
        order.total_price = order.apply_promocode()
    else:
        order.total_price = order.starting_price
    order.order_status = OrderStatus.ASSEMBLY


def get_in_delivery(order: Order) -> None:
    order.courier = choice(DB.get_free_couriers(order.urgency))
    order.courier.status = CourierStatus.DELIVERING
    order.order_status = OrderStatus.READY_FOR_DELIVERY


def finish_order(order: Order) -> None:
    order.courier.status = CourierStatus.FREE
    order.order_status = OrderStatus.DELIVERED


if __name__ == '__main__':
    # магазины
    shop_1 = DB.create_shop(name='Vkusvill')
    shop_2 = DB.create_shop(name='Magnit')
    shop_3 = DB.create_shop(name='Lenta')

    # продукты
    product1 = DB.create_good(product_name='apple', description='green apple')
    product2 = DB.create_good(product_name='apple', description='red apple')
    product3 = DB.create_good(product_name='chocolate', description='bitter chocolate 100g')
    product4 = DB.create_good(product_name='ba-na-na-ba-na-na-nas', description='-')
    product5 = DB.create_good(product_name='manga', description='yellow sweet manga')

    # формируем список продуктов в соответствующем магазине
    prod_available_1 = DB.create_product(product=product1, shop=shop_1, amount=12, price=23.20)
    prod_available_2 = DB.create_product(product=product1, shop=shop_2.id, amount=3, price=24.00)
    prod_available_3 = DB.create_product(product=product2, shop=shop_2, amount=5, price=25.50)
    prod_available_4 = DB.create_product(product=product3, shop=shop_3.id, amount=8, price=105)
    prod_available_5 = DB.create_product(product=product4, shop=shop_3, amount=25, price=15.35)
    prod_available_6 = DB.create_product(product=product5, shop=shop_3, amount=4, price=180.50)
    prod_available_7 = DB.create_product(product=product5, shop=shop_2.id, amount=2, price=155.60)

    # список товаров в выбранном магазине
    for i in DB.get_shops_list():
        print(i, sep='\n')
        for j in DB.get_products_in_shop(i):
            print(j)

    # клиенты
    client_1 = DB.create_client(name='Vanya', surname='Petrov', address='Ukhtomskogo 21',
                                mail='Petr234@mail.ru', phone='987539487')
    client_2 = DB.create_client(name='Petr', surname='Ivanov', phone='987534112',
                                mail='Ivan1@mail.ru', address='Uglicheskay 5')

    # добавление/удаление продуктов из корзины
    client_2.add_to_cartlist(product=prod_available_3, count=2)
    client_1.add_to_cartlist(product=prod_available_6, count=3)
    client_1.add_to_cartlist(product=prod_available_5, count=5)
    client_1.add_to_cartlist(product=prod_available_4, count=9)
    client_1.add_to_cartlist(product=prod_available_2, count=3)
    client_1.del_from_cartlist(product=prod_available_1)
    client_1.del_from_cartlist(product=prod_available_5)

    # администратор(создает и выдает промокоды клиентам)
    admin = Admin()
    new_promo1 = admin.generate_promocode(percent=10)
    admin.send_promocode(clients=[client_1], promocode=new_promo1)
    new_promo2 = admin.generate_promocode(5)
    admin.send_promocode(clients=[client_1, client_2], promocode=new_promo2)

    # формирование заказа
    order_1 = checkout(client=client_1, payment=Payment.CASH, address='Gromova 71',
                       promocode=new_promo2, urgency=Urgency.ASAP)
    order_2 = checkout(client=client_2, payment=Payment.CARD, address=client_2.address,
                       promocode=new_promo2, urgency=Urgency.URGENT)

    # курьеры
    courier_1 = DB.create_courier(courier_name="Stepan", courier_surname="Musorskiy",
                                  age=34, urgency=Urgency.URGENT)
    courier_2 = DB.create_courier(courier_name="Ivanessa", courier_surname="Kuznetsova", age=21)
    courier_3 = DB.create_courier(courier_name="Vladimir", courier_surname="Sokolov", age=56,
                                  urgency=Urgency.URGENT)
    courier_4 = DB.create_courier(courier_name="Nikolay", courier_surname="Novikovische", age=42)
    courier_5 = DB.create_courier(courier_name="Vasiliy", courier_surname="Morozov", age=38,
                                  urgency=Urgency.URGENT)

    # сборка, доставка заказа 1
    print('Order1:')
    print(order_1)
    collect_order(order_1)
    get_in_delivery(order_1)
    finish_order(order_1)
    print('Order1:')
    print(order_1)

    # оставить отзыв на продукт
    client_1.add_review(product3, mark_star=Star_mark.EXCELLENT, review_text='very tasty')
    print(product3.see_review())

    # сборка,доставка заказа 2
    collect_order(order_2)
    get_in_delivery(order_2)
    # просмотр статуса курьера
    print(courier_5.check_status())
    finish_order(order_2)
    print('Order2:')
    print(order_2)
