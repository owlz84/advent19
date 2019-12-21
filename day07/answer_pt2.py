from Amplifier import FeedbackOptimiser


if __name__ == "__main__":
    with open("data/software", "r") as fh:
        software = fh.read()
    optimiser = FeedbackOptimiser(software, 5, range(5, 10))
    optimiser.optimise()
    print(sorted(optimiser.results))
