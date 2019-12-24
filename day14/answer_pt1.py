from day14.ReactionCalculator import Calculator


if __name__ == "__main__":
    with open("data/puzzle_input", "r") as fh:
        calculator = Calculator(fh.read().splitlines())
    print(calculator.ore_requirement)
