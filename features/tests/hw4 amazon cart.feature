# Created by fritzbonheur at 6/8/23
Feature: Amazon Cart Verification

  Scenario: Verify item added to cart
    Given Open amazon main page
    When Open cart page
    Then Verify cart has {expected_count} item(s)
    Then Verify cart has correct product

