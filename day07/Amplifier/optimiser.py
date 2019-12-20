from typing import List
from itertools import permutations
from . import Amplifier


class Optimiser:
    def __init__(self, software: str, n_amps: int, phase_range: List[int]):
        self.software = software
        self.trials = list(permutations(phase_range, n_amps))
        self.results = list()

    def run(self):
        for phase_seq in self.trials:
            signals = list()
            for ix, phase in enumerate(phase_seq):
                signal = 0 if ix == 0 else signals[-1]
                amplifier = Amplifier(self.software, phase, signal)
                signals.append(amplifier())
            self.results.append((signals[-1], phase_seq))

    @property
    def best(self):
        return sorted(self.results)[-1][1]
