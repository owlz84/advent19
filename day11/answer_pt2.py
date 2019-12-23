from day11.MoonSimulator import Simulator


if __name__ == "__main__":
    with open("data/puzzle_input", "r") as fh:
        simulator = Simulator(fh.read().splitlines())
        simulator.output_interval = 10000
        print(simulator.system_period)
