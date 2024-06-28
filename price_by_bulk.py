# Feature No. 2 Calculate price of products sold in bulk

from prices import priceList


def calculate_price_by_bulk(totalPrice, product, weight):
    if isinstance(weight, (int, float, complex)):
        if product.lower() in list(priceList.keys()):
            totalPrice += priceList[product].price * weight

    return totalPrice
