import unittest
from glob import glob
from day09.OpcodeComputer import Computer


class OpcodeComputerTestCase(unittest.TestCase):
    def test_day02_tests(self):
        for fl in glob("../../day05/data/day02test*"):
            with open(fl, "r") as fh:
                test_data = fh.read().splitlines()
            computer = Computer(test_data[0])
            try:
                computer.run()
            except StopIteration:
                pass
            self.assertEqual([int(val) for val in test_data[1].split(",")], computer.program)

    def test_day05_tests(self):
        for fl in glob("../../day05/data/day05test*"):
            with open(fl, "r") as fh:
                test_data = fh.read().splitlines()
            computer = Computer(test_data[0])
            try:
                computer.run()
            except StopIteration:
                pass
            self.assertEqual([int(val) for val in test_data[1].split(",")], computer.program)

    def test_inputoutput(self):
        computer = Computer("3,0,4,0,99")
        try:
            computer.run().send(1337)
        except StopIteration:
            pass
        self.assertEqual(1337, computer.output[-1])

    def test_day05_part01_fullprogram(self):
        with open("../../day05/data/full_program", "r") as fh:
            test_data = fh.read()
        computer = Computer(test_data)
        try:
            computer.run().send(1)
        except StopIteration:
            pass
        self.assertEqual(5346030, computer.output[-1])

    def test_day05_part02_equality(self):
        with open("../../day05/data/day05equalitytest01", "r") as fh:
            for test_data in fh.read().splitlines():
                test_cases = zip([7, 8, 9], [0, 1, 0])
                for test_input, expected_outcome in test_cases:
                    computer = Computer(test_data)
                    try:
                        computer.run().send(test_input)
                    except StopIteration:
                        pass
                    self.assertEqual(expected_outcome, computer.output[-1])

    def test_day05_part02_inequality(self):
        with open("../../day05/data/day05equalitytest02", "r") as fh:
            for test_data in fh.read().splitlines():
                test_cases = zip([7, 8, 9], [1, 0, 0])
                for test_input, expected_outcome in test_cases:
                    computer = Computer(test_data)
                    try:
                        computer.run().send(test_input)
                    except StopIteration:
                        pass
                    self.assertEqual(expected_outcome, computer.output[-1])

    def test_day05_part02_jumps(self):
        with open("../../day05/data/day05jumptests", "r") as fh:
            for test_data in fh.read().splitlines():
                test_cases = zip([0, 1, -1], [0, 1, 1])
                for test_input, expected_outcome in test_cases:
                    computer = Computer(test_data)
                    try:
                        computer.run().send(test_input)
                    except StopIteration:
                        pass
                    self.assertEqual(expected_outcome, computer.output[-1])

    def test_day05_part02_bigtest(self):
        with open("../../day05/data/day05part02test", "r") as fh:
            test_data = fh.read()
            test_cases = zip([7, 8, 9], [999, 1000, 1001])
            for test_input, expected_outcome in test_cases:
                computer = Computer(test_data)
                try:
                    computer.run().send(test_input)
                except StopIteration:
                    pass
                self.assertEqual(expected_outcome, computer.output[-1])


if __name__ == '__main__':
    unittest.main()
