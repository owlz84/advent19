from day09.IntcodeComputer import Computer


if __name__ == "__main__":
    with open("data/full_boost", "r") as fh:
        program = fh.read()
    computer = Computer(program)
    computer.run().send(2)
    print(computer.output)
