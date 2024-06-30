Feature: Scan products and produce receipt
    Scenario Outline: Scan set of products having 1 normal, 1 completed b1g1, and/or 1 incomplete b1g1
        Given I have started the checkout counter with a list of salesPromotions:
            | product | promo |
            | <product0>  | <discount0> |
            | <product1>  | <discount1> |
        When I scan the group of products:
            | name     | bulk | promo | price |
            | <name0>  | <bulk0> | <promo0> | <price0> |
            | <name1>  | <bulk1> | <promo1> | <price1> |
            | <name2>  | <bulk2> | <promo2> | <price2> |
            | <name3>  | <bulk3> | <promo3> | <price3> |
        Then <totalPrice> is calculated
        And a full receipt is printed for the customer

        Examples:
            | name0 | bulk0 | promo0 | price0 | name1 | bulk1 | promo1 | price1 | name2 | bulk2 | promo2 | price2 | name3 | bulk3 | promo3 | price3 | product0 | product1 | discount0 | discount1 | totalPrice |
            | chocolate | - | b1g1 | 20 | bag_of_chips | - | - | 35 | chocolate | - | b1g1 | 20 | chocolate | - | b1g1 | 20 | chocolate | bottled_water | b1g1 | b2g1 | 75.0 |  
            | chocolate | - | b1g1 | 20 | bag_of_chips | - | - | 35 | chocolate | - | b1g1 | 20 | bag_of_chips | - | - | 35 | chocolate | bottled_water | b1g1 | b2g1 | 90.0 |
    
    Scenario Outline: Scan set of products having 1 normal, 2 bulks, 1 completed b1g1, and/or 1 incomplete b1g1 and b1g2
        Given I have started the checkout counter with a list of salesPromotions:
            | product | promo |
            | <product0>  | <discount0> |
            | <product1>  | <discount1> |
        When I scan the group of products:
            | name     | bulk | promo | price |
            | <name0>  | <bulk0> | <promo0> | <price0> |
            | <name1>  | <bulk1> | <promo1> | <price1> |
            | <name2>  | <bulk2> | <promo2> | <price2> |
            | <name3>  | <bulk3> | <promo3> | <price3> |
        Then <totalPrice> is calculated
        And a full receipt is printed for the customer

        Examples:
            | name0 | bulk0 | promo0 | price0 | name1 | bulk1 | promo1 | price1 | name2 | bulk2 | promo2 | price2 | name3 | bulk3 | promo3 | price3 | product0 | product1 | discount0 | discount1 | totalPrice |
            | bag_of_rice | 1 | - | 45 | bag_of_chips | - | - | 35 | pack_of_sugar | 0.25 | - | 20 | chocolate | - | b1g1 | 20 | chocolate | bottled_water | b1g1 | b2g1 | 110.0 |  
            | bag_of_rice | 1 | - | 45 | bottled_water | - | b2g1 | 15 | pack_of_sugar | 0.25 | - | 20 | chocolate | - | b1g1 | 20 | chocolate | bottled_water | b1g1 | b2g1 | 90.0 |  
            