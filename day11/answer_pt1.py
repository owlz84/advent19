from day11.MoonSimulator import Simulator


if __name__ == "__main__":
    with open("data/puzzle_input", "r") as fh:
        simulator = Simulator(fh.read().splitlines())
        simulator.run(1000)
        print(simulator.total_energy)
