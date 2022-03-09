Feature: 
    As a report owner,
    I want to see descriptive numbers of the amount of money,
    So that I can get insights on amount of money.

    Scenario: Get total amount of momey
        Given the source data "money_details.csv"

        When the csv file is passed to the get total amount of money process

        Then the process should return the sum of money

    Scenario: Get total amount of money of people in the Public Utilities sector that are from Portugal
        Given the source data "money_details.csv" and "client_details.csv" 

        When the csv file is passed to the get total amount of money of people in the Public Utilities sector that are from Portugal process

        Then the process should join the money and client data on id 
        
        And return the sum of money from the id's that have "sector" = "Public Utilities" and "country" = "Portugal"

    Scenario: Get total amount of money of people in the Finance sector that are from the Netherlands
        Given the source data "money_details.csv" and "client_details.csv" 

        When the csv file is passed to the get total amount of money of people in the Finance sector that are from the Netherlands process

        Then the process should join the money and client data on id 
        
        And return the sum of money from the id's that have "sector" = "Finance" and "country" = "Netherlands"
