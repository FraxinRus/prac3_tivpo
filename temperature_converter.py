def temperature_converter(amount, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return amount * 9 / 5 + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (amount - 32) * 5 / 9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return amount + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return amount - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (amount - 32) * 5 / 9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (amount - 273.15) * 9 / 5 + 32
    else:
        return amount * 2
