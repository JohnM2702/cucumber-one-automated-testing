from behave import given, when, then
from price_by_bulk import calculate_price_by_bulk


@given('I have started the checkout counter for bulk')
def openCheckoutCounterBulk(context):
    context.totalPrice = 0
    context.product = "bag_of_rice"
    context.weight = 0.5


@when('I add a $product with a $weight')
def addBulkProduct(context):
    context.totalPrice += calculate_price_by_bulk(
        context.totalPrice, context.product, context.weight)


@then('$totalPrice is updated for bulk')
def totalBulkPriceUpdate(context):
    assert context.totalPrice == float(45*0.5)
