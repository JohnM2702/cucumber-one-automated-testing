# Feature No. 4 Scan products and print receipt

from price_by_piece import calculate_price_by_piece
from price_by_bulk import calculate_price_by_bulk
from price_by_sale import calculate_price_by_sale


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
    "assorted_candies": Product("assorted_candies", 27.0),
    "bag_of_rice": BulkProduct("bag_of_rice", 45, 1),
    "pack_of_sugar": BulkProduct("pack_of_sugar", 20, 0.5),
    "chocolate": SaleProduct("chocolate", 20, "b1g1"),
    "bottled_water": SaleProduct("bottled_water", 15, "b2g1"),
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

        i = 0
        for product in products:
            if isinstance(product, BulkProduct):
                try:
                    prod = priceList[product.name]
                    result = calculate_price_by_bulk(priceList, totalPrice, prod, float(product.quantity))
                    price_by_item[product.name+"-"+str(i)] = (product.quantity, None, result-totalPrice)
                    totalPrice = result
                except:
                    pass
                    
            elif isinstance(product, SaleProduct) and product.name in list(self.salesPromotions.keys()):
                result, p_type, ssp = calculate_price_by_sale(
                    self.priceList, self.salesPromotions, totalPrice, scannedSaleProducts, product)

                if result != "Resource Not Found":
                    if p_type == "incomplete":
                        scannedSaleProducts = ssp
                    elif p_type == "complete":
                        scannedSaleProducts = ssp
                        amount = "2" if product.promotions == "b1g1" else "3"
                        price_by_item[product.name+f" x({amount})"+"-"+str(i)] = (None, product.promotions, product.price)
                        totalPrice = result
                    
            elif isinstance(product, Product):
                result = calculate_price_by_piece(priceList, totalPrice, product)
                if result != "Resource Not Found":
                    price_by_item[product.name+"-"+str(i)] = (None, None, product.price)
                    totalPrice = result
            
            i += 1
        

        # Process scannedSaleProducts if there are any products from incomplete promos
        for product in scannedSaleProducts:
            result = calculate_price_by_piece(priceList, totalPrice, product)
            if result != "Resource Not Found":
                price_by_item[product.name+"-"+str(i)] = (None, product.promotions, product.price)
                totalPrice = result

        receipt = self.generate_receipt(price_by_item)
        return totalPrice, receipt

    def generate_receipt(self, scannedProducts):
        receipt = "\n|\tProduct\t\tWeight\tPromo\tPrice\t|\n"
        for item in list(scannedProducts.keys()):
            entry = ""
            temp = item.split("-")[0]
            if scannedProducts[item][0]: entry = f"|\t{temp}\t{scannedProducts[item][0]}\t-\t{scannedProducts[item][-1]}\t|"
            elif scannedProducts[item][1]: entry = f"|\t{temp}\t-\t{scannedProducts[item][1]}\t{scannedProducts[item][-1]}\t|"
            else: entry = f"|\t{temp}\t-\t-\t{scannedProducts[item][-1]}\t|"
            receipt += entry + "\n"
        print(receipt)
        return receipt
