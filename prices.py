class Product:
    def __init__(self, n, p):
        self.name = n
        self.price = p


class BulkProduct(Product):
    def __init__(self, n, p, q):
        super().__init__(n, p)
        self.quantity = q


class SaleProduct(Product):
    def __init__(self, n, p, pr):
        super().__init__(n, p)
        self.promotions = pr


# prod = BulkProduct()

# print(type())

priceList = {
    "bag_of_chips": Product("bag_of_chips", 35.0),
    "bag_of_rice": BulkProduct("bag_of_rice", 45, 1),
    "chocolate": SaleProduct("chocolate", 20, "b1g1"),
    "bottled_water": SaleProduct("bottled_water", 15, "b2g1")
}


promotions = {
    "chocolate": "b1g1",
    "bottled_water": "b2g1"
}
