# Created by fritzbonheur at 7/17/23
Feature: # CureSkin price filter
  Scenario: # Verify price filter functionality
    Given Open CureSkin Home page
    Then Click on Shop All section
    And Adjust Price Filter
    Then Verify # of products changes
    When Verify products are within Price Filter