from typing import List
from operator import mul, add, lt, eq


class Instruction:
    def __init__(self, code: int, param_modes: List[int]):
        self.code = code
        self.param_modes = param_modes

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


class Computer:
    def __init__(self, program: str):
        self.run_ix = 0
        self.input = 0
        self.output = 0
        self.program = [int(val) for val in program.split(",")]
        print(self.program)
        self.ops = [
            None, self.addition_op, self.multiplication_op,
            self.input_op, self.output_op,
            self.jump_if_true_op, self.jump_if_false_op,
            self.less_than_op, self.equal_to_op
        ]

    @staticmethod
    def parse_instruction(instruction):
        instruction_str = str(instruction)
        instruction_str_padded = "0" * (5-len(instruction_str)) + instruction_str
        code = int(instruction_str_padded[-2:])
        param_modes = [int(val) for val in reversed(instruction_str_padded[:3])]
        return Instruction(
            code=code,
            param_modes=param_modes
        )

    def get_value(self, ix, param_mode):
        return self.program[ix] if param_mode == 0 else ix

    def set_value(self, ix, val):
        self.program[ix] = val

    def addition_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.set_value(params[-1], add(*values[:2]))
        print(f"> result: {add(*values[:2])} stored to: {params[-1]}")

    def multiplication_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.set_value(params[-1], mul(*values[:2]))
        print(f"> result: {mul(*values[:2])} stored to: {params[-1]}")

    def input_op(self, params: List[int], param_modes: List[int]) -> None:
        self.set_value(params[-1] , self.input)

    def output_op(self, params: List[int], param_modes: List[int]) -> None:
        self.output = self.get_value(params[-1], param_modes[0])

    def jump(self, mode: bool, val: int, ix: int):
        self.run_ix = self.run_ix if mode ^ (val != 0) else ix

    def jump_if_true_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.jump(True, *values)

    def jump_if_false_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.jump(False, *values)

    def less_than_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.set_value(params[-1], 1 if lt(*values[:2]) else 0)

    def equal_to_op(self, params: List[int], param_modes: List[int]) -> None:
        values = [self.get_value(val, mode) for val, mode in zip(params, param_modes)]
        print(f"> parameter values: {values}")
        self.set_value(params[-1], 1 if eq(*values[:2]) else 0)

    def run(self):
        while self.run_ix < len(self.program):
            print(f"\nindex: {self.run_ix}\n> instruction: {self.program[self.run_ix]}")
            parsed_instruction = self.parse_instruction(self.program[self.run_ix])
            if parsed_instruction.code == 99:
                return
            op = self.ops[parsed_instruction.code]
            params = self.program[self.run_ix+1:][:parsed_instruction.length-1]
            print(f"> instruction code: {parsed_instruction.code}, parameters: {params}, parameter modes: {parsed_instruction.param_modes}")
            self.run_ix += parsed_instruction.length
            op(params, parsed_instruction.param_modes)


