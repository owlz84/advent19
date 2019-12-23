import unittest
from day11.MoonSimulator import Simulator


class EnergyTest01(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test1", "r") as fh:
            self.sensor_data = fh.read().splitlines()

    def test_simulator_energy(self):
        simulator = Simulator(self.sensor_data)
        simulator.run(10)
        self.assertEqual(179, simulator.total_energy)


class EnergyTest02(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test2", "r") as fh:
            self.sensor_data = fh.read().splitlines()

    def test_simulator_energy(self):
        simulator = Simulator(self.sensor_data)
        simulator.run(100)
        self.assertEqual(1940, simulator.total_energy)


if __name__ == '__main__':
    unittest.main()
