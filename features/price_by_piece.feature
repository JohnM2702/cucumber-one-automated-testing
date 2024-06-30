Feature: Calculating price of products sold by piece
    Scenario Outline: Scan a normal product
        Given I have started the checkout counter
        When I add a <product0>
            | name | price |
            | <product0> | <price0> |
        Then <totalPrice> is updated
    
        Examples:
            | product0 | price0 | totalPrice |
            | bag_of_chips | 35.0 | 35.0 |
            | assorted_candies | 27.0 | 27.0 |
    
    Scenario Outline: Scan a product that does not exist in the database
        Given I have started the checkout counter
        When I add a <product0>
            | name | price |
            | <product0> | <price0> |
        Then <totalPrice> is not updated

        Examples:
            | product0 | price0 | totalPrice |
            | ice_cream | 50.0 | 35.0 |
