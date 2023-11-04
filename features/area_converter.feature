Feature: Area Converter

  Scenario: Convert from Square Kilometer to Hectare
    Given the value is 10
    When converting from Square Kilometer to Hectare
    Then the result should be 1000.0 on Hectare

  Scenario: Convert from Square Kilometer to Decare
    Given the value is 10
    When converting from Square Kilometer to Decare
    Then the result should be 10000.0 on Decare

  Scenario: Convert from Hectare to Square Kilometer
    Given the value is 10
    When converting from Hectare to Square Kilometer
    Then the result should be 0.1 on Square Kilometer

  Scenario: Convert from Hectare to Decare
    Given the value is 10
    When converting from Hectare to Decare
    Then the result should be 100.0 on Decare

  Scenario: Convert from Decare to Square Kilometer
    Given the value is 10
    When converting from Decare to Square Kilometer
    Then the result should be 0.01 on Square Kilometer

  Scenario: Convert from Decare to Hectare
    Given the value is 10
    When converting from Decare to Hectare
    Then the result should be 1.0 on Hectare

  Scenario: Convert within the same area system
    Given the value is 10
    When converting within the same area system
    Then the result should be the same
