import sqlite3 as sql
from order import Order

db = sql.connect('data.db')
c = db.cursor()


def add_products(p_sh_a):
    c.execute(f"INSERT INTO availability VALUES ('{p_sh_a.product}',"
              f"'{p_sh_a.shop}','{p_sh_a.amount}',"
              f"'{p_sh_a.price}')")


def product_base():
    c.execute(f"SELECT rowid, * FROM availability")
    items = c.fetchall()
    return items


def add_clients(client):
    c.execute(f"INSERT INTO clients VALUES ('{client.name}',"
              f"'{client.surname}','{client.phone}',"
              f"'{client.mail}')")


def clients_base():
    c.execute(f"SELECT rowid, * FROM clients")
    items = c.fetchall()
    return items


def add_couriers(courier):
    c.execute(f"INSERT INTO couriers VALUES ('{courier.name}',"
              f"'{courier.surname}','{courier.age}',"
              f"'{courier.urgency},{courier.status},{courier.cnt_order}')")


def couriers_base():
    c.execute(f"SELECT rowid, * FROM couriers")
    items = c.fetchall()
    return items


""""
def add_orders(order):
    c.execute(f"INSERT INTO orders VALUES {order}")


def orders_base():
    c.execute(f"SELECT rowid, * FROM orders")
    items = c.fetchall()
    return items
    """
