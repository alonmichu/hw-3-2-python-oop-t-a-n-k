from decimal import Decimal
from functools import wraps
from typing import Dict, Callable, Union, List
from uuid import UUID, uuid4

from client import Client
from courier import Courier, Urgency
from order import Order, Payment
from product import Product
from productShopAvailability import ProductShopAvailability
from promocode import Promocode
from shop import Shop


class SingletonMeta(type):
    _instance = None

    def __call__(mcs, *args, **kwargs):
        if not mcs._instance:
            mcs._instance = super(SingletonMeta, mcs).__call__(*args, **kwargs)
        return mcs._instance


class Container:
    def __init__(self, obj_type):
        self._obj_type = obj_type
        self._container: Dict[UUID, obj_type] = dict()

    def delete(self, identifier: UUID) -> bool:
        if identifier in self._container:
            del self._container[identifier]
            return True
        return False

    def __delitem__(self, key: UUID) -> bool:
        return self.delete(key)

    def add(self, identifier: UUID, obj, update: bool = False) -> Union[None, Callable]:
        if type(obj) != self._obj_type:
            return None
        if identifier in self._container:
            if update:
                self._container[identifier] = obj
                return obj
            return None
        else:
            self._container[identifier] = obj
            return obj

    def __setitem__(self, key, value) -> Union[None, Callable]:
        return self.add(key, value)

    def find(self, identifier: UUID) -> Union[Callable, None]:
        return self._container.get(identifier, None)

    def __getitem__(self, item) -> Union[Callable, None]:
        return self.find(item)


class PythonDb(metaclass=SingletonMeta):

    def __init__(self):
        self.orders: Container = Container(Order)
        self.products: Container = Container(ProductShopAvailability)
        self.couriers: Container = Container(Courier)
        self.clients: Container = Container(Client)
        self.shops: Container = Container(Shop)

        self._obj_container = {
            Order: self.orders,
            ProductShopAvailability: self.products,
            Courier: self.couriers,
            Client: self.clients,
            Shop: self.shops,
        }
        self._uuid_container: Dict[UUID] = dict()

    def _add_uuid(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            if res is not None:
                self._uuid_container[res.id] = self._obj_container[type(res)]
            return res

        return wrapper

    @_add_uuid
    def create_from_obj(self, obj: Union[Order, ProductShopAvailability, Courier, Client]) \
            -> Union[Order, ProductShopAvailability, Courier, Client, Shop, None]:
        if type(obj) in self._obj_container:
            self._obj_container[type(obj)].add(obj.id, obj)
            return self._obj_container[type(obj)].find(obj.id)

    @_add_uuid
    def create_product(self, product: Product, shop: Union[Shop, UUID], amount: int,
                       price: float) -> Union[ProductShopAvailability, None]:
        prod_uuid = uuid4()
        return self.products.add(
            prod_uuid,
            ProductShopAvailability(
                product_id=prod_uuid,
                product=product,
                shop=shop.id if isinstance(shop, Shop) else shop,
                amount=amount,
                price=Decimal(price),
            )
        )

    @_add_uuid
    def create_courier(self, courier_name: str, courier_surname: str, age: int, cnt_order: int) \
            -> Union[Courier, None]:
        courier_uuid = uuid4()
        return self.couriers.add(courier_uuid, Courier(
            courier_id=courier_uuid,
            name=courier_name,
            surname=courier_surname,
            age=age,
            cnt_order=cnt_order

        ))

    @_add_uuid
    def create_client(self, name: str, surname: str, phone: str, mail: str) \
            -> Union[Client, None]:
        client_uuid = uuid4()
        return self.clients.add(client_uuid, Client(
            client_id=client_uuid,
            name=name,
            surname=surname,
            phone=phone,
            mail=mail
        ))

    @_add_uuid
    def create_order(self, product_list: List[Union[ProductShopAvailability, UUID]],
                     promocode: Promocode = None, payment: Payment = Payment.CARD,
                     urgency: Urgency = Urgency.ASAP) -> Union[Order, None]:
        product_list = [product.id if isinstance(product, ProductShopAvailability)
                        else product for product in product_list]
        order_uuid = uuid4()
        return self.orders.add(order_uuid, Order(
            order_id=order_uuid,
            product_list=product_list,
            promocode=promocode,
            payment=payment,
            urgency=urgency
        ))

    @_add_uuid
    def create_shop(self, name: str) -> Union[Shop, None]:

        shop_uuid = uuid4()
        return self.shops.add(shop_uuid, Shop(
            shop_id=shop_uuid,
            shop_name=name
        ))
