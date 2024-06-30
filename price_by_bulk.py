# Feature No. 2 Calculate price of products sold in bulk

def calculate_price_by_bulk(priceList, totalPrice, product, weight):
    if isinstance(product.quantity, (int, float, complex)):
        if product.name.lower() in list(priceList.keys()):
            totalPrice += priceList[product.name].price * (float(weight/product.quantity))
        else:
            return totalPrice 

    return totalPrice
