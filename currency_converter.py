def currency_converter(amount, from_currency, to_currency):
    if from_currency == 'USD' and to_currency == 'RUB':  # USD -> RUB
        return amount * 92.7325
    elif from_currency == 'USD' and to_currency == 'EUR':  # USD -> EUR
        return amount * 0.947
    elif from_currency == 'USD' and to_currency == 'VND':  # USD -> VND
        return amount * 24580
    elif from_currency == 'RUB' and to_currency == 'VND':  # RUB -> VND
        return amount * 2.6545417
    else:
        return 'Invalid input'
