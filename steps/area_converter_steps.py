from behave import given, when, then
from area_converter import area_converter

@given('the value is {value}')
def set_value(context, value):
    context.value = float(value)

@when('converting from Square Kilometer to Hectare')
def convert_sqkm_to_hectare(context):
    context.result = area_converter(context.value, 0, 1)

@when('converting from Square Kilometer to Decare')
def convert_sqkm_to_decare(context):
    context.result = area_converter(context.value, 0, 2)

@when('converting from Hectare to Square Kilometer')
def convert_hectare_to_sqkm(context):
    context.result = area_converter(context.value, 1, 0)

@when('converting from Hectare to Decare')
def convert_hectare_to_decare(context):
    context.result = area_converter(context.value, 1, 2)

@when('converting from Decare to Square Kilometer')
def convert_decare_to_sqkm(context):
    context.result = area_converter(context.value, 2, 0)

@when('converting from Decare to Hectare')
def convert_decare_to_hectare(context):
    context.result = area_converter(context.value, 2, 1)

@when('converting within the same area system')
def convert_within_same_system(context):
    context.result = area_converter(context.value, 0, 0)

@then('the result should be {expected_result} on Hectare')
def check_hectare_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be {expected_result} on Decare')
def check_decare_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be {expected_result} on Square Kilometer')
def check_sqkm_result(context, expected_result):
    expected_result = float(expected_result)
    assert context.result == expected_result

@then('the result should be the same')
def check_same_system(context):
    assert context.result == context.value
