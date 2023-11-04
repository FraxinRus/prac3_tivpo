Feature: Power Converter

Scenario: Convert from SI to American System
  Given the value is 10
  When converting from SI to American System
  Then the result should be 2.25 on American System

Scenario: Convert from SI to Russian System
  Given the value is 10
  When converting from SI to Russian System
  Then the result should be 0.06 on Russian System

Scenario: Convert from American System to SI
  Given the value is 10
  When converting from American System to SI
  Then the result should be 44.48 on SI

Scenario: Convert from American System to Russian System
  Given the value is 10
  When converting from American System to Russian System
  Then the result should be 0.28 on Russian System

Scenario: Convert from Russian System to SI
  Given the value is 10
  When converting from Russian System to SI
  Then the result should be 1606.38 on SI

Scenario: Convert from Russian System to American System
  Given the value is 10
  When converting from Russian System to American System
  Then the result should be 361.13 on American System

Scenario: Convert within the same system
  Given the value is 10
  When converting within the same system
  Then the result should be the same