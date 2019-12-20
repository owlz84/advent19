import unittest
from glob import glob
from .OpcodeComputer import Computer


class MyTestCase(unittest.TestCase):
    def test_day02_tests(self):
        for fl in glob("day05/data/day02test*"):
            with open(fl, "r") as fh:
                test_data = fh.read().splitlines()
            computer = Computer(test_data[0])
            computer.run()
            self.assertEqual([int(val) for val in test_data[1].split(",")], computer.program)


if __name__ == '__main__':
    unittest.main()
