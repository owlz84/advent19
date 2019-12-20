from typing import List
from operator import mul, add, lt, eq


class Computer:
    def __init__(self, program: str):
        self.run_ix = 0
        self.cycles = 0
        self.input = list()
        self.input_counter = 0
        self.output = 0
        self.program = [int(val) for val in program.split(",")]
        self.ops = [
            None, self.addition_op, self.multiplication_op,
            self.input_op, self.output_op,
            self.jump_if_true_op, self.jump_if_false_op,
            self.less_than_op, self.equal_to_op
        ]

    def add_input(self, new_input: int):
        self.input.append(new_input)

    def set_value(self, ix, val):
        self.program[ix] = val

    def addition_op(self, instruction) -> None:
        self.set_value(instruction.params[-1], add(*instruction.values[:2]))

    def multiplication_op(self, instruction) -> None:
        self.set_value(instruction.params[-1], mul(*instruction.values[:2]))

    def input_op(self, instruction) -> None:
        self.set_value(instruction.params[-1], self.input[min(len(self.input)-1, self.input_counter)])
        self.input_counter += 1

    def output_op(self, instruction) -> None:
        self.output = instruction.values[0]

    def jump(self, mode: bool, val: int, ix: int):
        self.run_ix = self.run_ix if mode ^ (val != 0) else ix

    def jump_if_true_op(self, instruction) -> None:
        self.jump(True, *instruction.values)

    def jump_if_false_op(self, instruction) -> None:
        self.jump(False, *instruction.values)

    def less_than_op(self, instruction) -> None:
        self.set_value(instruction.params[-1], 1 if lt(*instruction.values[:2]) else 0)

    def equal_to_op(self, instruction) -> None:
        self.set_value(instruction.params[-1], 1 if eq(*instruction.values[:2]) else 0)

    class Instruction:
        def __init__(self, instruction: int, memory: List[int]):
            self.raw_instruction = str(instruction)
            self.memory = memory
            self.code = None
            self.param_modes = None
            self.params = None
            self.parse_instruction()

        def parse_instruction(self):
            instruction_str_padded = "0" * (5 - len(self.raw_instruction)) + self.raw_instruction
            self.code = int(instruction_str_padded[-2:])
            self.param_modes = [int(val) for val in reversed(instruction_str_padded[:3])]

        @property
        def length(self):
            if self.code in [1, 2, 7, 8]:
                return 4
            elif self.code in [3, 4]:
                return 2
            elif self.code in [5, 6]:
                return 3
            else:
                return 0

        def get_value(self, ix, param_mode):
            return self.memory[ix] if param_mode == 0 else ix

        @property
        def values(self):
            return [self.get_value(val, mode) for val, mode in zip(self.params, self.param_modes)]

    def run(self):
        self.cycles = 0
        while self.run_ix < len(self.program):
            parsed_instruction = self.Instruction(self.program[self.run_ix], self.program)
            if parsed_instruction.code == 99:
                return
            op = self.ops[parsed_instruction.code]
            parsed_instruction.params = self.program[self.run_ix+1:][:parsed_instruction.length-1]
            self.run_ix += parsed_instruction.length
            op(parsed_instruction)
            self.cycles += 1
