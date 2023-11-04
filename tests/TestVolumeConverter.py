import unittest
from volume_converter import volume_converter

class TestVolumeConverter(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(volume_converter(1, 1, 2), 0.26) # литры -> галлоны
        self.assertEqual(volume_converter(1, 1, 3), 0.81) # литры -> штофы
        self.assertEqual(volume_converter(1, 2, 1), 3.79) # галлоны -> литры
        self.assertEqual(volume_converter(1, 2, 3), 3.08) # галлоны -> штофы
        self.assertEqual(volume_converter(1, 3, 1), 1.23) # штофы -> литры
        self.assertEqual(volume_converter(1, 3, 2), 0.32) # штофы -> галлоны
        self.assertEqual(volume_converter(1, 1, 1), 1) # литры -> литры
        self.assertEqual(volume_converter(1, 2, 2), 1) # галлоны -> галлоны
        self.assertEqual(volume_converter(1, 3, 3), 1) # штофы -> штофы


if __name__ == '__main__':
    unittest.main()
