# Created by fritzbonheur at 7/17/23
Feature: # CureSkin price filter
  Scenario: # Verify price filter functionality
    Given Open CureSkin Home page
    Then Click on Shop All section
    Then Adjust Price Filter
    Then Verify products Change
    When Verify products are within Price Filter