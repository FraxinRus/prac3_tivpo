import unittest
from length_converter import length_converter


class TestLengthConverter(unittest.TestCase):
    def test_length(self):
        self.assertEqual(length_converter(10, 0, 1), 0.39)
        self.assertEqual(length_converter(10, 0, 2), 8.2)
        self.assertEqual(length_converter(10, 1, 0), 25.4)
        self.assertEqual(length_converter(10, 1, 2), 21.1)
        self.assertEqual(length_converter(10, 2, 0), 12.2)
        self.assertEqual(length_converter(10, 2, 1), 4.7)
        self.assertEqual(length_converter(10, 0, 0), 10)


if __name__ == '__main__':
    unittest.main()
