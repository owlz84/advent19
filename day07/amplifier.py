class Amplifier:
    def __init__(self, a0: int, software: str):
        self.a0 = a0
        self.software = software.split(",")

    @property
    def max_signal(self):
        return 0


if __name__ == "__main__":
    print()
