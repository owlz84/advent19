import unittest
from day09.IntcodeComputer import Computer


class BoostTestCase(unittest.TestCase):
    def test_boost1(self):
        with open("../data/test_prog1", "r") as fh:
            test_prog = fh.read()
        computer = Computer(test_prog)
        computer.run()
        self.assertEqual([int(val) for val in test_prog.split(",")], computer.output)

    def test_boost2(self):
        with open("../data/test_prog2", "r") as fh:
            computer = Computer(fh.read())
        computer.run()
        self.assertEqual(16, len(str(computer.output[0])))

    def test_boost3(self):
        with open("../data/test_prog3", "r") as fh:
            computer = Computer(fh.read())
        computer.run()
        self.assertEqual(1125899906842624, computer.output[0])

    def test_boost4(self):
        computer = Computer("109,-1,4,1,99")
        computer.run()
        self.assertEqual(-1, computer.output[0])

    def test_boost5(self):
        computer = Computer("109, -1, 104, 1, 99")
        computer.run()
        self.assertEqual(1, computer.output[0])

    def test_boost6(self):
        computer = Computer("109, -1, 204, 1, 99")
        computer.run()
        self.assertEqual(109, computer.output[0])

    def test_boost7(self):
        computer = Computer("109, 1, 9, 2, 204, -6, 99")
        computer.run()
        self.assertEqual(204, computer.output[0])

    def test_boost8(self):
        computer = Computer("109, 1, 109, 9, 204, -6, 99")
        computer.run()
        self.assertEqual(204, computer.output[0])

    def test_boost8(self):
        computer = Computer("109,1,209,-1,204,-106,99")
        computer.run()
        self.assertEqual(204, computer.output[0])


if __name__ == '__main__':
    unittest.main()
