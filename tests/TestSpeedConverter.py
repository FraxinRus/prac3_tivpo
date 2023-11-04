import unittest
from speed_converter import speed_converter


class TestSpeedConverter(unittest.TestCase):
    def test_speed(self):
        self.assertEqual(speed_converter(10, 0, 1), 2.78)
        self.assertEqual(speed_converter(10, 0, 2), 6.21)
        self.assertEqual(speed_converter(10, 1, 0), 36)
        self.assertEqual(speed_converter(10, 1, 2), 22.37)
        self.assertEqual(speed_converter(10, 2, 0), 16.09)
        self.assertEqual(speed_converter(10, 2, 1), 4.47)
        self.assertEqual(speed_converter(10, 0, 0), 10)


if __name__ == '__main__':
    unittest.main()
