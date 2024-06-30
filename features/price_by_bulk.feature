Feature: Calculating price of products sold by bulk
    Scenario Outline: Scan a product sold in bulk
        Given I have started the checkout counter for bulk
        When I add a <product0> with a <quantity0> quantity
            | name | price | quantity |
            | <product0> | <price0> | <quantity0> |
        Then <totalPrice> is updated
    
        Examples:
            | product0 | price0 | quantity0 | totalPrice |
            | bag_of_rice | 45.0 | 1.0 | 45.0 |
            | bag_of_rice | 45.0 | 2.0 | 90.0 |
            | pack_of_sugar | 20.0 | 0.25 | 10.0 |
            | pack_of_sugar | 20.0 | 0.5 | 20.0 |
            | pack_of_sugar | 20.0 | 1.0 | 40.0 |
    
    Scenario Outline: Scan a product sold in bulk that does not exist in the database
        Given I have started the checkout counter for bulk
        When I add a <product0> with a <quantity0> quantity
            | name | price | quantity |
            | <product0> | <price0> | <quantity0> |
        Then <totalPrice> is not updated
    
        Examples:
            | product0 | price0 | quantity0 | totalPrice |
            | bag_of_peanuts | 100.0 | 1.0 | 57.0 |
    