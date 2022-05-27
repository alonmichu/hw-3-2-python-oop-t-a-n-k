from decimal import Decimal
from functools import wraps
from typing import Dict, Callable, Union, List
from uuid import UUID, uuid4

from client import Client
from courier import Courier, Urgency, CourierStatus
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

    def get_all(self):
        return list(self._container.values())

    def values(self):
        return self._container.values()


class PythonDb(metaclass=SingletonMeta):

    def __init__(self):
        self.orders: Container = Container(Order)
        self.products: Container = Container(ProductShopAvailability)
        self.couriers: Container = Container(Courier)
        self.clients: Container = Container(Client)
        self.shops: Container = Container(Shop)
        self.goods: Container = Container(Product)

        self._obj_container = {
            Order: self.orders,
            ProductShopAvailability: self.products,
            Courier: self.couriers,
            Client: self.clients,
            Shop: self.shops,
            Product: self.goods
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
        prod_shop_av = ProductShopAvailability(
                product_id=prod_uuid,
                product=product,
                shop=shop.id if isinstance(shop, Shop) else shop,
                amount=amount,
                price=Decimal(price)
        )
        self.products.add(prod_uuid, prod_shop_av)
        return prod_shop_av

    @_add_uuid
    def create_courier(self, courier_name: str, courier_surname: str,
                       age: int, urgency: Urgency = Urgency.ASAP) -> Union[Courier, None]:
        courier_uuid = uuid4()
        courier = Courier(
            courier_id=courier_uuid,
            name=courier_name,
            surname=courier_surname,
            age=age,
            urgency=urgency
        )
        self.couriers.add(courier_uuid, courier)
        return courier

    @_add_uuid
    def create_client(self, name: str, surname: str, phone: str, mail: str, address: str) \
            -> Union[Client, None]:
        client_uuid = uuid4()
        client = Client(
            client_id=client_uuid,
            name=name,
            surname=surname,
            address=address,
            mail=mail,
            phone=phone
        )
        self.clients.add(client_uuid, client)
        return client

    @_add_uuid
    def create_order(self, address: str, client_obj: Client,
                     payment: Payment = Payment.CARD,
                     promocode: Promocode = None,
                     urgency: Urgency = Urgency.ASAP) -> Union[Order, None]:

        product_list = client_obj.cart_list

        order_uuid = uuid4()
        order = Order(
            order_id=order_uuid,
            address=address,
            product_list=product_list,
            promocode=promocode,
            payment=payment,
            urgency=urgency,
            client_id=client_obj.id
        )
        self.orders.add(order_uuid, order)
        return order

    @_add_uuid
    def create_shop(self, name: str) -> Union[Shop, None]:

        shop_uuid = uuid4()
        shop = Shop(
            shop_id=shop_uuid,
            shop_name=name
        )
        self.shops.add(shop_uuid, shop)
        return shop

    @_add_uuid
    def create_good(self, product_name: str, description: str = None) -> Union[Product, None]:

        product_uuid = uuid4()
        product = Product(
            product_id=product_uuid,
            product_name=product_name,
            description=description
        )
        self.goods.add(product_uuid, product)
        return product

    def get_shops_list(self) -> List[Shop]:
        return self.shops.get_all()

    def get_products_in_shop(self, shop: Union[UUID, Shop]) -> List[ProductShopAvailability]:
        shop_id = shop if isinstance(shop, UUID) else shop.id
        return [product for product in self.products.values() if product.shop == shop_id]

    def get_free_couriers(self, urgency: Urgency) -> List[Courier]:
        available_couriers = []
        for courier in self.couriers.values():
            if courier.urgency == urgency and courier.status == CourierStatus.FREE:
                available_couriers.append(courier)
        return available_couriers
