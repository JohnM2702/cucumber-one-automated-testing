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


prod = BulkProduct()

print(type())
priceList = {
    "bag_of_chips": 35.0
}
