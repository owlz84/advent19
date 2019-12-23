from typing import List
from operator import mul, add, lt, eq
from coroutine import coroutine


class Computer:
    def __init__(self, program: str):
        self.run_ix = 0
        self.input = 0
        self.output = list()
        self.relative_base = 0
        self.program = [int(val) for val in program.split(",")] + [0 for i in range(10000)]
        self.ops = [
            None, self.addition_op, self.multiplication_op,
            self.input_op, self.output_op,
            self.jump_if_true_op, self.jump_if_false_op,
            self.less_than_op, self.equal_to_op,
            self.set_relative_base
        ]
        self.target = None

    def set_value(self, ix, val):
        self.program[ix] = val

    def addition_op(self, instruction) -> None:
        self.set_value(instruction.write_index, add(*instruction.values[:2]))

    def multiplication_op(self, instruction) -> None:
        self.set_value(instruction.write_index, mul(*instruction.values[:2]))

    def input_op(self, instruction) -> None:
        self.set_value(instruction.write_index, self.input)

    def output_op(self, instruction) -> None:
        self.output.append(instruction.values[0])

    def jump(self, mode: bool, val: int, ix: int):
        self.run_ix = self.run_ix if mode ^ (val != 0) else ix

    def jump_if_true_op(self, instruction) -> None:
        self.jump(True, *instruction.values)

    def jump_if_false_op(self, instruction) -> None:
        self.jump(False, *instruction.values)

    def less_than_op(self, instruction) -> None:
        self.set_value(instruction.write_index, 1 if lt(*instruction.values[:2]) else 0)

    def equal_to_op(self, instruction) -> None:
        self.set_value(instruction.write_index, 1 if eq(*instruction.values[:2]) else 0)

    def set_relative_base(self, instruction) -> None:
        self.relative_base += instruction.values[-1]

    class Instruction:
        def __init__(self, instruction: int, memory: List[int], relative_base: int):
            self.raw_instruction = str(instruction)
            self.memory = memory
            self.relative_base = relative_base
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
            elif self.code in [3, 4, 9]:
                return 2
            elif self.code in [5, 6]:
                return 3
            else:
                return 0

        def get_value(self, ix, param_mode):
            offset = self.relative_base if param_mode == 2 else 0
            return ix if param_mode == 1 else self.memory[ix + offset]

        @property
        def values(self):
            return [self.get_value(val, mode) for val, mode in zip(self.params, self.param_modes)]

        @property
        def write_index(self):
            return self.params[-1] + (self.relative_base if self.param_modes[self.length-2] == 2 else 0)

    @coroutine
    def run(self):
        while True:
            parsed_instruction = self.Instruction(self.program[self.run_ix], self.program, self.relative_base)
            if parsed_instruction.code == 3:
                self.input = (yield)
            if parsed_instruction.code == 99:
                yield self.output
            op = self.ops[parsed_instruction.code]
            parsed_instruction.params = self.program[self.run_ix+1:][:parsed_instruction.length-1]
            self.run_ix += parsed_instruction.length
            op(parsed_instruction)
            if parsed_instruction.code == 4 and self.target:
                try:
                    self.target().send(self.output)
                except StopIteration:
                    yield self.output
