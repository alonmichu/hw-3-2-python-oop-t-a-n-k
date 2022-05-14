from decimal import Decimal
from functools import wraps
from typing import Dict, Callable, Union, List
from uuid import UUID

from client import Client
# from utils import get_logger
from courier import Courier, Urgency
from order import Order, Payment
from product import Product
from productShopAvailability import ProductShopAvailability
from promocode import Promocode
from shop import Shop


# logger = get_logger(__name__)


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
            # logger.debug(f'{identifier} successfully found and deleted from container')
            return True
        # logger.debug(f'{identifier} not found in container')
        return False

    def __delitem__(self, key: UUID) -> bool:
        return self.delete(key)

    def add(self, identifier: UUID, obj, update: bool = False) -> Union[None, Callable]:
        if type(obj) != self._obj_type:
            # logger.warning(f'Types mismatched ({identifier})')
            return None
        if identifier in self._container:
            # logger.info(f'Object with {identifier} already exists!')
            if update:
                self._container[identifier] = obj
                # logger.info(f'Object was overwritten')
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
        # self.shops: Container = Container(Shop)
        self.clients: Container = Container(Client)

        self._obj_container = {
            Order: self.orders,
            ProductShopAvailability: self.products,
            Courier: self.couriers,
            # Shop: self.shops,
            Client: self.clients,
        }
        self._uuid_container: Dict[UUID] = dict()

    def _add_uuid(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            if res is not None:
                self._uuid_container[res._id] = self._obj_container[type(res)]
            return res

        return wrapper

    @_add_uuid
    def create_from_obj(self, obj: Union[Order, ProductShopAvailability, Courier, Client]) \
            -> Union[Order, ProductShopAvailability, Courier, Client, None]:
        if type(obj) in self._obj_container:
            self._obj_container[type(obj)].add(obj._id, obj)
            return self._obj_container[type(obj)].find(obj._id)

    @_add_uuid
    def create_product(self, product: Product, shop: Union[Shop, UUID], amount: int, price: float) \
            -> Union[ProductShopAvailability, None]:
        cur_product = ProductShopAvailability(
            product=product,
            shop=shop,
            amount=amount,
            price=Decimal(price),
        )
        return self.products.add(cur_product.id, cur_product)

    @_add_uuid
    def create_courier(self, courier_name: str, courier_surname: str, age: int, cnt_order: int) \
            -> Union[Courier, None]:
        courier = Courier(
            name=courier_name,
            surname=courier_surname,
            age=age,
            cnt_order=cnt_order

        )

        return self.couriers.add(courier.id, courier)

    @_add_uuid
    def create_client(self, name: str, surname: str, phone: str, mail: str) \
            -> Union[Client, None]:
        client = Client(
            name=name,
            surname=surname,
            phone=phone,
            mail=mail
        )
        return self.users.add(client.id, client)

    @_add_uuid
    def create_order(self, product_list: List[ProductShopAvailability, UUID], promocode: Promocode = None,
                     payment: Payment = Payment.CARD, urgency: Urgency = Urgency.ASAP) -> Union[Order, None]:

        order = Order(
            product_list=product_list,
            promocode=promocode,
            payment=payment,
            urgency=urgency
        )

        return self.orders.add(order.id, order)
