class Shop:

    def __init__(self, shop_id, shop_name: str):
        self.id = shop_id
        self.name = shop_name

    def __str__(self):
        return f"{self.name}"
