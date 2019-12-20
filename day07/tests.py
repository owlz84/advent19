import unittest
from Amplifier import Amplifier, Optimiser


class MyTestCase(unittest.TestCase):
    def test_amplifier_mechanics1(self):
        with open("data/part1_test1_software", "r") as fh:
            test_software = fh.read()
        phase_seq = [4, 3, 2, 1, 0]
        signals = list()
        for ix, phase in enumerate(phase_seq):
            signal = 0 if ix == 0 else signals[-1]
            amplifier = Amplifier(test_software, phase, signal)
            signals.append(amplifier())
        self.assertEqual(43210, signals[-1])

    def test_amplifier_mechanics2(self):
        with open("data/part1_test2_software", "r") as fh:
            test_software = fh.read()
        phase_seq = [0, 1, 2, 3, 4]
        signals = list()
        for ix, phase in enumerate(phase_seq):
            signal = 0 if ix == 0 else signals[-1]
            amplifier = Amplifier(test_software, phase, signal)
            signals.append(amplifier())
        self.assertEqual(54321, signals[-1])

    def test_optimiser1(self):
        with open("data/part1_test1_software", "r") as fh:
            test_software = fh.read()
        optimiser = Optimiser(test_software, 5, range(5))
        optimiser.run()
        self.assertEqual((4, 3, 2, 1, 0), optimiser.best)

    def test_optimiser2(self):
        with open("data/part1_test2_software", "r") as fh:
            test_software = fh.read()
        optimiser = Optimiser(test_software, 5, range(5))
        optimiser.run()
        self.assertEqual((0, 1, 2, 3, 4), optimiser.best)

    def test_optimiser3(self):
        with open("data/part1_test3_software", "r") as fh:
            test_software = fh.read()
        optimiser = Optimiser(test_software, 5, range(5))
        optimiser.run()
        self.assertEqual((1, 0, 4, 3, 2), optimiser.best)


if __name__ == '__main__':
    unittest.main()
