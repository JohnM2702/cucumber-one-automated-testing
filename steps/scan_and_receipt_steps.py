from behave import given, when, then
from GroceryStore import promotions, priceList, sampleProducts, GroceryStore


@given("I have started the checkout counter with a list of $salesPromotions for a product list")
def openCheckoutCounterMain(context):
    context.salesPromotions = promotions
    context.products = sampleProducts


@when("I scan the group of $products")
def scanProducts(context):
    groceryStore = GroceryStore(priceList, promotions)
    context.totalPrice, context.receipt = groceryStore.scan_products(
        context.products)


@then("$totalPrice of products is calculated")
def totalProductsPriceUpdate(context):
    print(context.totalPrice)
    assert context.totalPrice == 65
