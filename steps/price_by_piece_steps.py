from behave import given, when, then
from price_by_piece import calculate_price_by_piece
from GroceryStore import priceList, Product


@given('I have started the checkout counter')
def openCheckoutCounter(context):
    context.totalPrice = 0.0
    context.priceList = priceList

@when('I add a {product:S}')
def addProduct(context, product):
    product = Product(context.table[0]['name'], context.table[0]['price'])
    context.totalPrice = calculate_price_by_piece(context.priceList, context.totalPrice, product)

@then('{totalPrice:f} is updated')
def totalPriceUpdate(context, totalPrice):
    assert context.totalPrice == totalPrice

@then('{totalPrice:f} is not updated')
def totalPriceUpdate(context, totalPrice):
    assert context.totalPrice != totalPrice
