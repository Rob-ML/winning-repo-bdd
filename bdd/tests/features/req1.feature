Feature: 
    As a report owner,
    I want to see descriptive numbers of my clients,
    So that I can get insights on my clients.

    Scenario: Get total number of clients
        Given the source data

        When the client detail is passed to the get total number of clients process

        Then the process should return the sum of the distinct id's

    Scenario: Get the subtotals for clients in the Transportation sector
        Given the source data
        
        When the client detail is passed to the get subtotal number of clients in the transportation sector process

        Then the process should return the sum of distinct id's that have "sector" = "Transportation"

    Scenario: Get the subtotals for clients in in the Health Sector that use credit cards from JCB
        Given the source data

        When the client detaul is passed to the get subtotal number of clients in the Health Sector with Credit Cards from JCB

        Then the process should return the sum of distinct id's that have "sector" = "Health Care" and "credit_card_type" = "jcb"

    