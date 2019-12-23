import unittest
from day11.MoonSimulator import Simulator


class RepeatTest01(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test1", "r") as fh:
            self.sensor_data = fh.read().splitlines()

    def test_simulator_repeat(self):
        simulator = Simulator(self.sensor_data)
        simulator.output_interval = 10000
        self.assertEqual(2772, simulator.system_period)


class RepeatTest02(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test2", "r") as fh:
            self.sensor_data = fh.read().splitlines()

    def test_simulator_repeat(self):
        simulator = Simulator(self.sensor_data)
        simulator.output_interval = 10000
        self.assertEqual(4686774924, simulator.system_period)


if __name__ == '__main__':
    unittest.main()
