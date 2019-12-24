import unittest
from day14.ReactionCalculator import Calculator


class TestCase1(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test1", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_fuel_per_trillion_ore(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(34482758620, calculator.fuel_per_qty_ore(int(1e12)))


class TestCase2(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test2", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_fuel_per_trillion_ore(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(6323777402, calculator.fuel_per_qty_ore(int(1e12)))


class TestCase3(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test3", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_fuel_per_trillion_ore(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(82892753, calculator.fuel_per_qty_ore(int(1e12)))


class TestCase4(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test4", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_fuel_per_trillion_ore(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(5586022, calculator.fuel_per_qty_ore(int(1e12)))


class TestCase5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test5", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_fuel_per_trillion_ore(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(460664, calculator.fuel_per_qty_ore(int(1e12)))


if __name__ == '__main__':
    unittest.main()
