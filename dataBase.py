import sqlite3 as sql

db = sql.connect('data.db')
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS clients(
   client_id INT PRIMARY KEY,
   client BLOB);
""")
db.commit()
c.execute("""CREATE TABLE IF NOT EXISTS couriers(
   courier_id INT PRIMARY KEY,
   courier BLOB);
""")
db.commit()
c.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_id INT PRIMARY KEY,
    client_order BLOB);
""")

db.commit()
c.execute("""CREATE TABLE IF NOT EXISTS availability(
   product BLOB,
   shop BLOB,
   amount INTEGER,
   price REAL);
""")
db.commit()


def add_products(p_sh_a):
    c.execute(f"INSERT INTO availability VALUES ('{p_sh_a.product}',"
              f"'{p_sh_a.shop}','{p_sh_a.amount}',"
              f"'{p_sh_a.price}')")
    db.commit()


def product_base():
    c.execute(f"SELECT rowid, * FROM availability")
    items = c.fetchall()
    return items


def add_clients(client):
    c.execute("INSERT INTO clients VALUES(?);", client)
    db.commit()


def clients_base():
    c.execute(f"SELECT rowid, * FROM clients")
    items = c.fetchall()
    return items


def add_couriers(courier):
    c.execute("INSERT INTO couriers VALUES(?);", courier)
    db.commit()


def couriers_base():
    c.execute(f"SELECT rowid, * FROM couriers")
    items = c.fetchall()
    return items


def add_orders(new_order):
    c.execute("INSERT INTO orders VALUES(?);", new_order)
    db.commit()


def orders_base():
    c.execute(f"SELECT rowid, * FROM orders")
    items = c.fetchall()
    return items
