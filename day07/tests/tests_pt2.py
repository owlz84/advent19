import unittest
from Amplifier import Amplifier, Optimiser, FeedbackOptimiser


class MyTestCase(unittest.TestCase):
    def test_feedback_optimiser1(self):
        with open("data/part2_test1_software", "r") as fh:
            test_software = fh.read()
        optimiser = FeedbackOptimiser(test_software, 5, range(5, 10))
        optimiser.optimise()
        print(optimiser.best)
        self.assertEqual((9, 8, 7, 6, 5), optimiser.best)

    def test_feedback_optimiser2(self):
        with open("data/part2_test2_software", "r") as fh:
            test_software = fh.read()
        optimiser = FeedbackOptimiser(test_software, 5, range(5, 10))
        optimiser.optimise()
        print(optimiser.best)
        self.assertEqual((9, 7, 8, 5, 6), optimiser.best)


if __name__ == '__main__':
    unittest.main()
