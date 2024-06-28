Feature: Calculate price of products on sale
    Scenario: Scan a product on sale
        Given I have started the checkout counter with a list of $salesPromotions
        When I add a sale $product
        Then $totalPrice is updated with sale
