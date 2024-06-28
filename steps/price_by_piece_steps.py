from behave import given, when, then
from price_by_piece import calculate_price_by_piece
from prices import priceList, Product


@given('I have started the checkout counter')
def openCheckoutCounter(context):
    context.priceList = priceList
    context.totalPrice = 0
    context.product = Product("bag_of_chips", 35.0)


@ when('I add a $product')
def addProduct(context):
    context.totalPrice += calculate_price_by_piece(context.priceList,
                                                   context.totalPrice, context.product)


@ then('$totalPrice is updated')
def totalPriceUpdate(context):
    assert context.totalPrice == float(35)
