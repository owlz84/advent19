import unittest
from day10.MapReader import MapReader


class MapScanTest1(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test1_map", "r") as fh:
            self.test_input = fh.read().splitlines()
        with open("../data/test1_soln", "r") as fh:
            self.test_values = [[0 if char == "." else int(char) for char in line] for line in fh.read().splitlines()]

    def test_map_values(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual(self.test_values, map_reader.translated_map)

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual((3, 4), map_reader.best_location)


class MapScanTest2(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test2_map", "r") as fh:
            self.test_input = fh.read().splitlines()

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual((5, 8), map_reader.best_location)

    def test_num_visible(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual(33, map_reader.visible_from_best)


class MapScanTest3(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test3_map", "r") as fh:
            self.test_input = fh.read().splitlines()

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual((1, 2), map_reader.best_location)

    def test_num_visible(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual(35, map_reader.visible_from_best)


class MapScanTest4(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test4_map", "r") as fh:
            self.test_input = fh.read().splitlines()

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual((6, 3), map_reader.best_location)

    def test_num_visible(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual(41, map_reader.visible_from_best)


class MapScanTest5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test5_map", "r") as fh:
            self.test_input = fh.read().splitlines()

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual((11, 13), map_reader.best_location)

    def test_num_visible(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        self.assertEqual(210, map_reader.visible_from_best)


if __name__ == '__main__':
    unittest.main()
