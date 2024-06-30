Feature: Calculate price of products on sale
    Scenario Outline: Scan a product on sale (b1g1)
        Given I have started the checkout counter for a sale product with a list of salesPromotions:
            | product | promo |
            | <product0>  | <discount0> |
            | <product1>  | <discount1> |
        And the following products have been scanned having 55.0 amount:
            | name | bulk | promo | price |
            | chocolate | - | b1g1 | 20 |
            | bag_of_chips | - | - | 35 |
            | chocolate | - | b1g1 | 20 |
            | chocolate | - | b1g1 | 20 |
        When I add a sale product <name0>
            | name | price | promo |
            | <name0> | <price0> | <promo0> |
        Then <totalPrice> is updated

        Examples:
        | name0 | price0 | promo0 | product0 | product1 | discount0 | discount1 | totalPrice |
        | chocolate | 20 | b1g1 | chocolate | bottled_water | b1g1 | b2g1 | 75.0 |
    
    Scenario Outline: Scan a product on sale (b2g1)
        Given I have started the checkout counter for a sale product with a list of salesPromotions:
            | product | promo |
            | <product0>  | <discount0> |
            | <product1>  | <discount1> |
        And the following products have been scanned having 35.0 amount:
            | name | bulk | promo | price |
            | bottled_water | - | b2g1 | 15 |
            | bag_of_chips | - | - | 35 |
            | bottled_water | - | b2g1 | 15 |
        When I add a sale product <name0>
            | name | price | promo |
            | <name0> | <price0> | <promo0> |
        Then <totalPrice> is updated

        Examples:
        | name0 | price0 | promo0 | product0 | product1 | discount0 | discount1 | totalPrice |
        | bottled_water | 15 | b2g1 | chocolate | bottled_water | b1g1 | b2g1 | 65.0 |
