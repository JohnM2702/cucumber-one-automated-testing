# Feature No.3 Calculate price of products on sale

def calculate_price_by_sale(priceList, salesPromotions, totalPrice, scannedSaleProducts, product):
    p_name = product.name.lower()
    if p_name in list(priceList.keys()) and p_name in [p.lower() for p in salesPromotions.keys()]:
        promoStatus = None
        # Checks the scanned sale products that satisfy the covered promos
        if product.promotions == "b1g1":
            promoStatus = [p.name for p in scannedSaleProducts].count(
                product.name) >= 1
        elif product.promotions == "b2g1":
            promoStatus = [p.name for p in scannedSaleProducts].count(
                product.name) >= 2

        p_stat = "incomplete"
        # Checks if the promo was satisfied, if so apply the discount
        if promoStatus is True:
            product_indices = [i for i, p in enumerate(
                scannedSaleProducts) if p.name == product.name][:2]

            # Remove the first two elements with the same product name
            if product.promotions == "b1g1":
                del scannedSaleProducts[product_indices[0]]
                totalPrice += priceList[p_name].price
            elif product.promotions == "b2g1":
                del scannedSaleProducts[product_indices[0]]
                del scannedSaleProducts[product_indices[1] - 1]
                totalPrice += priceList[p_name].price*2

            p_stat = "complete"
        else:
            scannedSaleProducts.append(product)
        return totalPrice, p_stat, scannedSaleProducts
    else:
        return "Resource Not Found", None, None
