from Amplifier import Optimiser


if __name__ == "__main__":
    with open("data/software", "r") as fh:
        software = fh.read()
    optimiser = Optimiser(software, 5, range(5))
    optimiser.optimise()
    print(sorted(optimiser.results))
