import operator
from dataclasses import dataclass
from functools import reduce
from typing import Callable, List

from base import BaseSolution


@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    condition: Callable[[int], int]
    inspection_count: int = 0

    @classmethod
    def parse(cls, block):
        lines = block.splitlines()
        items = cls.parse_items(lines[1])
        operation = cls.parse_operation(lines[2])
        condition = cls.parse_condition(lines[3:])
        return cls(items, operation, condition)

    @classmethod
    def parse_items(cls, line):
        return [int(value) for value in line.split(": ")[-1].split(", ")]

    @classmethod
    def parse_operation(cls, line):
        lhs, op_char, rhs = line.split(" new = ")[-1].split()
        if op_char == "+":
            op_fn = operator.add
        if op_char == "*":
            op_fn = operator.mul

        lhs_fn = cls.parse_operation_val(lhs)
        rhs_fn = cls.parse_operation_val(rhs)

        def fn(old):
            return op_fn(lhs_fn(old), rhs_fn(old))

        return fn

    @classmethod
    def parse_operation_val(cls, expr_val):
        def fn(old):
            if expr_val == "old":
                return old
            return int(expr_val)

        return fn

    @classmethod
    def parse_condition(cls, lines):
        divisible_by = int(lines[0].split()[-1])
        if_true = int(lines[1].split()[-1])
        if_false = int(lines[2].split()[-1])

        def fn(value):
            if value % divisible_by == 0:
                return if_true
            return if_false

        return fn


class Solution(BaseSolution):
    def load_data(self, input):
        return [Monkey.parse(block) for block in input.split("\n\n")]

    def part1(self, data):
        self.do_rounds(data, 20)
        inspection_counts = sorted(
            (monkey.inspection_count for monkey in data), reverse=True
        )
        return reduce(operator.mul, inspection_counts[:2])

    def part2(self, data):
        pass

    # Helpers

    def do_rounds(self, data, num):
        for _ in range(num):
            self.do_round(data)

    def do_round(self, data):
        for monkey in data:
            while monkey.items:
                monkey.inspection_count += 1
                item = monkey.items.pop(0)
                worry = monkey.operation(item) // 3
                target = monkey.condition(worry)
                data[target].items.append(worry)
