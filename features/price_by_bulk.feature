Feature: Calculate price of products sold in bulk
    Scenario: Scan a product sold in bulk
        Given I have started the checkout counter for bulk
        When I add a $product with a $weight
        Then $totalPrice is updated for bulk

