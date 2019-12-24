import unittest
from day14.ReactionCalculator import Calculator


class TestCase1(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test1", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_ratio(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(31, calculator.ore_requirement)


class TestCase2(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test2", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_ratio(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(165, calculator.ore_requirement)


class TestCase3(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test3", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_ratio(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(13312, calculator.ore_requirement)


class TestCase4(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test4", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_ratio(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(180697, calculator.ore_requirement)


class TestCase5(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test5", "r") as fh:
            self.nanofactory_output = fh.read().splitlines()

    def test_ratio(self):
        calculator = Calculator(self.nanofactory_output)
        self.assertEqual(2210736, calculator.ore_requirement)


if __name__ == '__main__':
    unittest.main()
