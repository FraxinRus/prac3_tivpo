import unittest
from currency_converter import currency_converter


class TestCurrencyConverter(unittest.TestCase):
    def test_currency_converter(self):
        self.assertEqual(currency_converter(100, 'USD', 'RUB'), 9273.25)
        self.assertEqual(currency_converter(100, 'USD', 'EUR'), 94.7)
        self.assertEqual(currency_converter(100, 'USD', 'VND'), 2458000)
        self.assertEqual(currency_converter(1000, 'RUB', 'VND'), 265454.17)


if __name__ == '__main__':
    unittest.main()
