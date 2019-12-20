from OpcodeComputer import Computer


if __name__ == "__main__":
    with open("data/full_program", "r") as fh:
        computer = Computer(fh.read())
    computer.input = 5
    computer.optimise()
    print(computer.output)
