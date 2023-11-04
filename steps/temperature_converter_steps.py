from behave import given, when, then
from temperature_converter import temperature_converter


@given('the amount is {amount}')
def SetAmount(context, amount):
    context.amount = float(amount)


@when('convert from {from_unit} to {to_unit}')
def Convert(context, from_unit, to_unit):
    context.from_unit = from_unit
    context.to_unit = to_unit
    context.converted = temperature_converter(context.amount, context.from_unit, context.to_unit)


@then('the result should be {result} in {to_unit}')
def CheckResult(context, result, to_unit):
    assert context.converted == float(result)
