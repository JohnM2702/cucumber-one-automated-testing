Feature: Calculating price of products sold by piece
    Scenario: Scan a normal product
        Given I have started the checkout counter
        When I add a $product
        Then $totalPrice is updated
