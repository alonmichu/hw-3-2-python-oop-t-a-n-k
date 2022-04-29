# В этом файле пишем классы. Перед началом работы не забудьте сделать pull
from client import Client
from product import Product
from courier import Courier
from order import Order
from shop import Shop

test = Product('choco1ate', 'gfdfg')
print(test.__dict__)
print(test)
test.name = 'choco'
print(test.__dict__)

client_1 = Client('Vanya', 'Petrov', '987539487', 'Petr234@mail.ru')
print(client_1.__dict__)
client_1.name = 'Ivan'
client_1.phone = '9987524612'
print(client_1.__dict__)
client_1.add_review(test, 'tasty')
print(test.__dict__)

order = Order('124')
print(order.order_status)
print(order.starting_price)
order.starting_price = 100
print(order.starting_price)
order.product_list.append(2)
print(order.product_list)
print(order.__dict__)

courier = Courier("Stepan", "Musorskiy", 34, 0)
print(courier)
courier.surname = "Mussorgsky"
print(courier)
courier.check_status()
print("What's about urgency? They said ", courier.urgency)

shop_1 = Shop('Vkusvill')
shop_1.name = 'VkusVill'
print(shop_1)
