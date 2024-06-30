from behave import given, when, then
from collections import Counter
from GroceryStore import priceList, GroceryStore, Product, BulkProduct, SaleProduct


@given("I have started the checkout counter with a list of salesPromotions")
def openCheckoutCounterMain(context):
    context.salesPromotions = {}
    for row in context.table:
        context.salesPromotions[row['product']] = row['promo']

@when("I scan the group of products")
def scanProducts(context):
    groceryStore = GroceryStore(priceList, context.salesPromotions)

    context.products = []
    for row in context.table:
        product = None
        if row['bulk'] != "-": product = BulkProduct(row['name'], row['price'], row['bulk'])
        elif row['promo'] != "-": product = SaleProduct(row['name'], row['price'], row['promo'])
        else: product = Product(row['name'], row['price'])
        context.products.append(product)

    context.totalPrice, context.receipt = groceryStore.scan_products(context.products)

@then('{totalPrice:f} is calculated')
def totalProductsPriceUpdate(context, totalPrice):
    assert context.totalPrice == totalPrice

@then('a full receipt is printed for the customer')
def shouldProduceFullReceipt(context):
    context.scannedProducts = []
    for entry in context.receipt.split('\n')[2:-1]:
        item = entry.split('\t')[1:-1]
        product = None

        if item[1] != '-': product = BulkProduct(item[0], item[-1], item[1])
        elif item[2] != '-': 
            product = SaleProduct(item[0].split(' x(')[0], item[-1], item[2])
            if " x(" in item[0]:
                for i in range(1, int(item[0].split(' x(')[1][:-1])):
                    context.scannedProducts.append(product)    
        else: product = Product(item[0], item[-1])
        
        context.scannedProducts.append(product)

    assert Counter([p.name for p in context.scannedProducts]) == Counter([p.name for p in context.products])


