import unittest
from day08.ImageReader import ImageReader


class Day08Part2Tests(unittest.TestCase):
    def test_image_compile_quick(self):
        image_reader = ImageReader("0222112222120000", (2, 2))
        self.assertEqual([[0, 1], [1, 0]], image_reader.image.tolist())


if __name__ == '__main__':
    unittest.main()
