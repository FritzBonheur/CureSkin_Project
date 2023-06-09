# Created by fritzbonheur at 6/8/23
Feature: Amazon Bestsellers Verification

  Scenario: Bestsellers Link Verification
    Given Open amazon main page
    When Click best sellers button
    Then Verify links are present