# Created by fritzbonheur at 5/31/23
Feature: Amazon Cart tests
  New User sees Empty Cart when not Signed In

  Scenario: User Can see Empty Cart
    Given Open amazon main page
    When Click on Cart
    Then Verify elements are preset for Your Amazon Cart is empty
