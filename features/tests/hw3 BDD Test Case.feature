# Created by fritzbonheur at 5/31/23
Feature: Amazon Sign In Page tests
  New User sees Sign In when clicking on Returns & Orders button

  Scenario: User can see Sign In Page
    Given Open amazon main page
    When Click on Returns&Orders
    Then Verify elements are present