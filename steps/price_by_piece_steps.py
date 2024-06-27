from behave import given, when, then
from price_by_piece import calculate_price_by_piece


@given('I have started the checkout counter')
def openCheckoutCounter(context):
    context.product = "0"


@when('I add a $product')
def addProduct(context):
    context.totalPrice = calculate_price_by_piece(context.product)


@then('$totalPrice is updated')
def totalPriceUpdate(context):
    assert context.totalPrice == float(0)
