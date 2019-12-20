from day05.OpcodeComputer import Computer


class Amplifier:
    def __init__(self, software: str, phase: int, signal: int):
        self.computer = Computer(software)
        self.computer.add_input(phase)
        self.computer.add_input(signal)
        self.computer.run()

    def __call__(self):
        return self.computer.output
