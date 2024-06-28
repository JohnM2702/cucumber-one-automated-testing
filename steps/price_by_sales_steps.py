from behave import given, when, then
from price_by_sale import calculate_price_by_sale
from prices import priceList, promotions, SaleProduct


@given('I have started the checkout counter with a list of $salesPromotions')
def openCheckoutCounterSale(context):
    context.priceList = priceList
    context.salesPromotions = promotions
    context.totalPrice = 0
    context.scannedSaleProducts = [SaleProduct("chocolate", 20, "b1g1")]
    context.product = SaleProduct("chocolate", 20, "b1g1")


@when('I add a sale $product')
def addSaleProduct(context):
    result, status, ssp = calculate_price_by_sale(
        context.priceList, context.salesPromotions, context.totalPrice, context.scannedSaleProducts, context.product)
    context.totalPrice += result


@then('$totalPrice is updated with sale')
def totalSalePriceUpdate(context):
    assert context.totalPrice == 20
