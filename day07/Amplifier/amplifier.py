from day07.OpcodeComputer import Computer


class Amplifier:
    def __init__(self, software: str, phase: int):
        self.computer = Computer(software)
        self.coro().send(phase)

    def __call__(self, signal):
        try:
            self.coro().send(signal)
        except StopIteration:
            return self.computer.output

    @property
    def coro(self):
        return self.computer.run

    @property
    def target(self):
        return self.computer.target

    @target.setter
    def target(self, coro):
        self.computer.target = coro
