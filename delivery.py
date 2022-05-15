# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
from product import Product
from admin import Admin
from dataBase import PythonDb

DB = PythonDb()
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

client_1 = DB.create_client('Vanya', 'Petrov', '987539487', 'Petr234@mail.ru')
client_2 = DB.create_client('Petr', 'Ivanov', '987534112', 'Ivan1@mail.ru')
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

"""
order_1 = DB.checkout(client_1, Payment.CASH, new_promo2)
print(order_1)
order_2 = DB.checkout(client_2, Payment.CARD, new_promo1)
print(order_2)
courier = Courier("Stepan", "Musorskiy", 34, 0)
print(courier)
courier.surname = "Mussorgsky"
print(courier)
courier.check_status()
print("What's about urgency? They said ", courier.urgency)

"""
