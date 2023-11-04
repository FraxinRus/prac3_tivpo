Feature: Temperature Converter

  Scenario: Convert Fahrenheit to Celsius
    Given the amount is 50
    When convert from Fahrenheit to Celsius
    Then the result should be 10 in Celsius

  Scenario: Convert Celsius to Fahrenheit
    Given the amount is 10
    When convert from Celsius to Fahrenheit
    Then the result should be 50 in Fahrenheit

  Scenario: Convert Celsius to Kelvin
    Given the amount is 10
    When convert from Celsius to Kelvin
    Then the result should be 283.15 in Kelvin

  Scenario: Convert Kelvin to Celsius
    Given the amount is 283.15
    When convert from Kelvin to Celsius
    Then the result should be 10 in Celsius

  Scenario: Convert Fahrenheit to Kelvin
    Given the amount is 50
    When convert from Fahrenheit to Kelvin
    Then the result should be 283.15 in Kelvin

  Scenario: Convert Kelvin to Fahrenheit
    Given the amount is 283.15
    When convert from Kelvin to Fahrenheit
    Then the result should be 50 in Fahrenheit

  Scenario: Convert Fahrenheit to Fahrenheit
    Given the amount is 50
    When convert from Fahrenheit to Fahrenheit
    Then the result should be 50 in Fahrenheit

  Scenario: Convert within the same unit
    Given the amount is 50
    When convert from Fahrenheit to Fahrenheit
    Then the result should be 50 in Fahrenheit
