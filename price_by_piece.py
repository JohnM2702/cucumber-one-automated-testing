# Feature No. 1 Calculate price of products sold by piece

def calculate_price_by_piece(priceList, totalPrice, product):
    if product.name.lower() in list(priceList.keys()):
        totalPrice += priceList[product.name].price
    else:
        return "Resource Not Found"

    return totalPrice
