from price_by_piece import calculate_price_by_piece
from price_by_bulk import calculate_price_by_bulk
from price_by_sale import calculate_price_by_sale
from prices import *


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


priceList = {
    "bag_of_chips": Product("bag_of_chips", 35.0),
    "bag_of_rice": BulkProduct("bag_of_rice", 45, 1),
    "chocolate": SaleProduct("shampoo", 20, "b1g1"),
    "bottled_water": SaleProduct("bottled_water", 15, "b2g1")
}

sampleProducts = {
    "bag_of_rice": BulkProduct("bag_of_rice", 45, 1),
    "chocolate": SaleProduct("chocolate", 20, "b1g1"),
}

promotions = {
    "chocolate": "b1g1",
    "bottled_water": "b2g1"
}


class GroceryStore():
    def __init__(self, priceList, promotions):
        self.salesPromotions = promotions
        self.priceList = priceList
        self.scannedSaleProducts = []  # list of Products

    def scan_products(self, products):
        totalPrice = 0
        price_by_item = {}
        scannedSaleProducts = []

        for product in list(products.values()):
            if isinstance(product, BulkProduct):
                result = calculate_price_by_bulk(
                    totalPrice, product.name, product.quantity)
                if result != "Resource Not Found":
                    price_by_item[product.name] = (product.quantity, result)
                    totalPrice += result
            elif isinstance(product, SaleProduct) and product.name in list(self.salesPromotions.keys()):
                result, p_type, ssp = calculate_price_by_sale(
                    self.priceList, self.salesPromotions, totalPrice, scannedSaleProducts, product)

                if result != "Resource Not Found":
                    if p_type == "incomplete":
                        scannedSaleProducts = ssp
                    elif p_type == "complete":
                        scannedSaleProducts = ssp
                        price_by_item[product.name] = (
                            product.promotions, result)
                        totalPrice += result
            elif isinstance(product, Product):
                result = calculate_price_by_piece(
                    priceList, totalPrice, product.name)
                if result != "Resource Not Found":
                    price_by_item[product.name] = (result)
                    totalPrice += result

        # Process scannedSaleProducts if there are any products from incomplete promos
        for product in scannedSaleProducts:
            result = calculate_price_by_piece(
                self.priceList, totalPrice, product)
            price_by_item[product.name] = (result)
            totalPrice = result

        receipt = self.generate_receipt()
        return totalPrice, receipt

    def generate_receipt(self):
        return "temporary"


# GroceryStoreOne = GroceryStore(priceList, promotions)
# print(GroceryStoreOne.scan_products(sampleProducts))
