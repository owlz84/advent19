from day05.OpcodeComputer import Computer


class Amplifier:
    def __init__(self, software: str, phase: int):
        self.computer = Computer(software)
        self.computer.add_input(phase)

    def __call__(self, signal):
        self.computer.add_input(signal)
        self.computer.run()
        return self.computer.output
