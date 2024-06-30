from behave import given, when, then
from price_by_bulk import calculate_price_by_bulk
from GroceryStore import priceList, BulkProduct


@given('I have started the checkout counter for bulk')
def openCheckoutCounterBulk(context):
    context.totalPrice = 0
    context.priceList = priceList

@when('I add a {product:S} with a {quantity:f} quantity')
def addBulkProduct(context, product, quantity):
    try:
        product = priceList[context.table[0]['name']]
        context.totalPrice = calculate_price_by_bulk(context.priceList, context.totalPrice, product, quantity)
    except:
        # Scanned product was not found in the database
        pass
    
@then('{totalPrice:f} is updated')
def totalBulkPriceUpdate(context, totalPrice):
    assert context.totalPrice == totalPrice

@then('{totalPrice:f} is not updated')
def totalBulkPriceUpdate(context, totalPrice):
    assert context.totalPrice != totalPrice