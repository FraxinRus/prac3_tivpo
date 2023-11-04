from behave import given, when, then
from power_converter import power_converter

@given('the value is {value}')
def set_value(context, value):
    context.value = float(value)

@when('converting from SI to American System')
def convert_si_to_american(context):
    context.result = power_converter(context.value, 1, 2)

@when('converting from SI to Russian System')
def convert_si_to_russian(context):
    context.result = power_converter(context.value, 1, 3)

@when('converting from American System to SI')
def convert_american_to_si(context):
    context.result = power_converter(context.value, 2, 1)

@when('converting from American System to Russian System')
def convert_american_to_russian(context):
    context.result = power_converter(context.value, 2, 3)

@when('converting from Russian System to SI')
def convert_russian_to_si(context):
    context.result = power_converter(context.value, 3, 1)

@when('converting from Russian System to American System')
def convert_to_american(context):
    context.result = power_converter(context.value, 3, 2)

@when('converting within the same system')
def convert_within_same_system(context):
    context.result = power_converter(context.value, 1, 1)

@then('the result should be {expected_result} on American System')
def check_american_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be {expected_result} on Russian System')
def check_russian_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be {expected_result} on SI')
def check_si_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be the same')
def check_same_system(context):
    assert context.result == context.value