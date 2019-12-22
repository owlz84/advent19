import unittest
from day10.MapReader import MapReader


class MapScanTest5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test5_map", "r") as fh:
            self.test_input = fh.read().splitlines()

    def test_map_best(self):
        map_reader = MapReader(self.test_input)
        map_reader.calc_pairwise_angles()
        map_reader.calc_sweep_angles()
        self.assertEqual((8, 2), map_reader.destroy_them_with_lasers(200))


if __name__ == '__main__':
    unittest.main()
