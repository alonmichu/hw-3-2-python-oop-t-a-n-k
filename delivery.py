# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
from client import Client
from product import Product
from productShopAvailability import ProductShopAvailability
from shop import Shop
from admin import Admin
from decimal import Decimal
from order import Payment

shop_1 = Shop('Vkusvill')
shop_2 = Shop('Magnit')
shop_3 = Shop('Lenta')
p_1 = Product('apple', 'green apple')
p_2 = Product('apple', 'red apple')
p_3 = Product('chocolate', 'bitter chocolate 100g')
p_4 = Product('bananas', '-')
p_5 = Product('manga', 'yellow sweet manga')
p_sh_a_1 = ProductShopAvailability(p_1, shop_1, 12, Decimal(23.20))
p_sh_a_2 = ProductShopAvailability(p_1, shop_2, 3, Decimal(24.00))
p_sh_a_3 = ProductShopAvailability(p_2, shop_2, 5, Decimal(25.50))
p_sh_a_4 = ProductShopAvailability(p_3, shop_3, 8, Decimal(105))
p_sh_a_5 = ProductShopAvailability(p_4, shop_3, 25, Decimal(15.35))
p_sh_a_6 = ProductShopAvailability(p_5, shop_3, 4, Decimal(180.50))
p_sh_a_7 = ProductShopAvailability(p_5, shop_2, 2, Decimal(155.60))

client_1 = Client('Vanya', 'Petrov', '987539487', 'Petr234@mail.ru')
client_2 = Client('Petr', 'Ivanov', '987534112', 'Ivan1@mail.ru')
client_2.add_to_cartlist(p_sh_a_3)
client_1.add_to_cartlist(p_sh_a_6)
client_1.add_to_cartlist(p_sh_a_5)
client_1.add_to_cartlist(p_sh_a_4)
client_1.add_to_cartlist(p_sh_a_2)
client_1.del_from_cartlist(p_sh_a_1)
client_1.del_from_cartlist(p_sh_a_5)

admin = Admin()
new_promo1 = admin.generate_promocode(10)
admin.send_promocode([client_1], new_promo1)
new_promo2 = admin.generate_promocode(5)
admin.send_promocode([client_1, client_2], new_promo2)

order_1 = client_1.checkout(Payment.CASH,new_promo2)
print(order_1)
order_2 = client_2.checkout(Payment.CARD, new_promo1)
print(order_2)


"""
courier = Courier("Stepan", "Musorskiy", 34, 0)
print(courier)
courier.surname = "Mussorgsky"
print(courier)
courier.check_status()
print("What's about urgency? They said ", courier.urgency)

"""
