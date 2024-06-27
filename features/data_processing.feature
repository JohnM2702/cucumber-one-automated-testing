Feature: Data Processing
  Scenario: Validate data transformation
    Given the user has some raw data
    When the data is processed
    Then the processed data should meet the expected criteria