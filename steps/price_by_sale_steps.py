from behave import given, when, then
from price_by_sale import calculate_price_by_sale
from GroceryStore import Product, BulkProduct, SaleProduct, priceList


@given('I have started the checkout counter for a sale product with a list of salesPromotions')
def openCheckoutCounterSale(context):
    context.salesPromotions = {}
    for row in context.table:
        context.salesPromotions[row['product']] = row['promo']

@given('the following products have been scanned having {totalPrice:f} amount')
def openCheckoutCounterSale2(context, totalPrice):
    context.totalPrice = totalPrice
    context.scannedProducts = []
    for row in context.table:
        product = None
        if row['bulk'] != "-": product = BulkProduct(row['name'], row['price'], row['bulk'])
        elif row['promo'] != "-": product = SaleProduct(row['name'], row['price'], row['promo'])
        else: product = Product(row['name'], row['price'])
        context.scannedProducts.append(product)


@when('I add a sale product {product:S}')
def addSaleProduct(context, product):
    product = SaleProduct(context.table[0]['name'], context.table[0]['price'], context.table[0]['promo'])
    result, status, ssp = calculate_price_by_sale(
        priceList, context.salesPromotions, context.totalPrice, context.scannedProducts, product)
    context.totalPrice = result


@then('{totalPrice:f} is updated')
def totalSalePriceUpdate(context, totalPrice):
    print(totalPrice, context.totalPrice)
    assert context.totalPrice == totalPrice
