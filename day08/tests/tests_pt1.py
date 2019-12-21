import unittest
from day08.ImageReader import ImageReader


class Day08Part1Tests(unittest.TestCase):
    def test_image_check_quick(self):
        image_reader = ImageReader("123456789012", (2, 3))
        self.assertEqual(1, image_reader.check)


if __name__ == '__main__':
    unittest.main()
