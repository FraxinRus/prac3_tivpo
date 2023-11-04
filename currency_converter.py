def currency_converter(amount, from_currency, to_currency):
    if from_currency == 'USD' and to_currency == 'RUB':  # USD -> RUB
        return round(round(amount, 2) * 92.7325, 2)
    elif from_currency == 'USD' and to_currency == 'EUR':  # USD -> EUR
        return round(round(amount, 2) * 0.947, 2)
    elif from_currency == 'USD' and to_currency == 'VND':  # USD -> VND
        return round(round(amount, 2) * 24580, 2)
    elif from_currency == 'RUB' and to_currency == 'VND':  # RUB -> VND
        return round(round(amount, 2) * 265.46, 2)
    else:
        return 'Invalid input'
