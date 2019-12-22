from day09.OpcodeComputer import Computer


if __name__ == "__main__":
    with open("data/full_boost", "r") as fh:
        program = fh.read()
    computer = Computer(program)
    computer.run().send(1)
    print(computer.output)
