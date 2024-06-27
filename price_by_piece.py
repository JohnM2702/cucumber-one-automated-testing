# Feature No. 1 Calculate price of products sold by piece
from prices import priceList


def calculate_price_by_piece(product):
    totalPrice = 0

    if product.lower() in list(priceList.keys()):
        totalPrice += priceList[product]

    return totalPrice


# print(calculate_price_by_piece("bag_of_chips"))
