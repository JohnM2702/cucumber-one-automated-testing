Feature: Scan products and produce receipt
    Scenario: Scan set of products having multiple product types
        Given I have started the checkout counter with a list of $salesPromotions for a product list
        When I scan the group of $products
        Then $totalPrice of products is calculated
