import unittest
from .amplifier import Amplifier


class MyTestCase(unittest.TestCase):
    def test_amplifier(self):
        with open ("day07/data/test1_software", "r") as fh:
            test_software = fh.read()
        amplifier = Amplifier(0, test_software)
        max_signal = amplifier.max_signal
        self.assertEqual(43210, max_signal)


if __name__ == '__main__':
    unittest.main()
