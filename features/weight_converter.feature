Feature: Weight Converter

  Scenario: Convert from SI to American System
    Given the value is 10
    When converting from SI to American System
    Then the result should be 22.0 on American System

  Scenario: Convert from SI to Russian System
    Given the value is 10
    When converting from SI to Russian System
    Then the result should be 24.4 on Russian System

  Scenario: Convert from American System to SI
    Given the value is 10
    When converting from American System to SI
    Then the result should be 4.5 on SI

  Scenario: Convert from American System to Russian System
    Given the value is 10
    When converting from American System to Russian System
    Then the result should be 11.0 on Russian System

  Scenario: Convert from Russian System to SI
    Given the value is 10
    When converting from Russian System to SI
    Then the result should be 4.1 on SI

  Scenario: Convert from Russian System to American System
    Given the value is 10
    When converting from Russian System to American System
    Then the result should be 9.0 on American System

  Scenario: Convert within the same system
    Given the value is 10
    When converting within the same system
    Then the result should be the same