import unittest
from math import pi
from day10.AsteroidTools import MapReader, LaserGun


class ShootThroughMap5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/test5_map", "r") as fh:
            self.map_reader = MapReader(fh.read().splitlines())

    def test_laser(self):
        laser = LaserGun(
            location=self.map_reader.best_location,
            asteroids=self.map_reader.asteroids,
            phase=-(pi / 2)
        )
        self.assertEqual((8, 2), laser.destroy_them_with_lasers(200).coord)


if __name__ == '__main__':
    unittest.main()
