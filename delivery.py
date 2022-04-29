# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
from client import Client
from product import Product
from productShopAvailability import ProductShopAvailability
from courier import Courier
from shop import Shop
from dataBase import add_products, product_base, add_couriers, \
    couriers_base, add_clients, clients_base

shop_1 = Shop('Vkusvill')
shop_2 = Shop('Magnit')
shop_3 = Shop('Lenta')
p_1 = Product('apple', 'green apple')
p_2 = Product('apple', 'red apple')
p_3 = Product('chocolate', 'bitter chocolate 100g')
p_4 = Product('bananas', '-')
p_5 = Product('manga', 'yellow sweet manga')
p_sh_a_1 = ProductShopAvailability(p_1, shop_1, 12, 23.20)
add_products(p_sh_a_1)
p_sh_a_2 = ProductShopAvailability(p_1, shop_2, 3, 24.00)
add_products(p_sh_a_2)
p_sh_a_3 = ProductShopAvailability(p_2, shop_2, 5, 25.50)
add_products(p_sh_a_3)
p_sh_a_4 = ProductShopAvailability(p_3, shop_3, 8, 105)
add_products(p_sh_a_4)
p_sh_a_5 = ProductShopAvailability(p_4, shop_3, 25, 15.35)
add_products(p_sh_a_5)
p_sh_a_6 = ProductShopAvailability(p_5, shop_3, 4, 180.50)
add_products(p_sh_a_6)
p_sh_a_7 = ProductShopAvailability(p_5, shop_2, 2, 155.60)
add_products(p_sh_a_7)
print(product_base())

client_1 = Client('Vanya', 'Petrov', '987539487', 'Petr234@mail.ru')
add_clients(client_1)
print(clients_base())
client_1.add_to_cartlist(p_sh_a_6)
client_1.add_to_cartlist(p_sh_a_5)
client_1.add_to_cartlist(p_sh_a_4)
client_1.add_to_cartlist(p_sh_a_2)
client_1.del_from_cartlist(p_sh_a_1)
client_1.del_from_cartlist(p_sh_a_5)
print('\nList of products:')
for i in client_1.cart_list:
    print(i)
print(client_1.checkout(1))
#print(orders_base)

"""
courier = Courier("Stepan", "Musorskiy", 34, 0)
print(courier)
courier.surname = "Mussorgsky"
print(courier)
courier.check_status()
print("What's about urgency? They said ", courier.urgency)

"""
