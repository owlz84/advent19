import unittest
from day10.AsteroidTools import MapReader


class MapScanTest1(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test1_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())
        with open("../data/test1_soln", "r") as fh:
            self.test_values = [[0 if char == "." else int(char) for char in line] for line in fh.read().splitlines()]

    def test_map_values(self):
        self.assertEqual(self.test_values, self.map_reader.translated_map)

    def test_map_best(self):
        self.assertEqual((3, 4), self.map_reader.best_location.coord)


class MapScanTest2(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test2_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())

    def test_map_best(self):
        self.assertEqual((5, 8), self.map_reader.best_location.coord)

    def test_num_visible(self):
        self.assertEqual(33, self.map_reader.best_location.n_visible_asteroids)


class MapScanTest3(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test3_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())

    def test_map_best(self):
        self.assertEqual((1, 2), self.map_reader.best_location.coord)

    def test_num_visible(self):
        self.assertEqual(35, self.map_reader.best_location.n_visible_asteroids)


class MapScanTest4(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test4_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())

    def test_map_best(self):
        self.assertEqual((6, 3), self.map_reader.best_location.coord)

    def test_num_visible(self):
        self.assertEqual(41, self.map_reader.best_location.n_visible_asteroids)


class MapScanTest5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test5_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())

    def test_map_best(self):
        self.assertEqual((11, 13), self.map_reader.best_location.coord)

    def test_num_visible(self):
        self.assertEqual(210, self.map_reader.best_location.n_visible_asteroids)


if __name__ == '__main__':
    unittest.main()
