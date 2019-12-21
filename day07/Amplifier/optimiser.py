from typing import List
from itertools import permutations
from . import Amplifier


class Optimiser:
    def __init__(self, software: str, n_amps: int, phase_range: List[int]):
        self.software = software
        self.trials = list(permutations(phase_range, n_amps))
        self.results = list()

    def optimise(self):
        for phase_seq in self.trials:
            signals = list()
            for ix, phase in enumerate(phase_seq):
                signal = 0 if ix == 0 else signals[-1]
                amplifier = Amplifier(self.software, phase)
                signals.append(amplifier(signal))
            self.results.append((signals[-1], phase_seq))

    @property
    def best(self):
        return sorted(self.results)[-1][1]


class FeedbackOptimiser:
    def __init__(self, software: str, n_amps: int, phase_range: List[int]):
        self.software = software
        self.n_amps = n_amps
        self.trials = list(permutations(phase_range, n_amps))
        self.amplifiers = list()
        self.results = list()

    def optimise(self):
        for phase_seq in self.trials:
            amplifiers = [Amplifier(self.software, phase) for phase in phase_seq]
            for ix, amplifier in enumerate(amplifiers):
                amplifiers[ix].target = amplifiers[(ix + 1) % self.n_amps].coro
            amplifiers[0](0)
            self.results.append((amplifiers[4].computer.output, phase_seq))

    @property
    def best(self):
        return sorted(self.results)[-1][1]
