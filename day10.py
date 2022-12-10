from dataclasses import dataclass
from itertools import chain

from base import BaseSolution


@dataclass
class State:
    x: int = 1


def noop():
    def fn(state):
        return
        yield

    return fn


def addx(value):
    def fn(state):
        yield
        state.x += value

    return fn


class Solution(BaseSolution):
    def load_data(self, input):
        return [self.parse_instruction(line) for line in input.splitlines()]

    def part1(self, data):
        state = State()
        cycle = 1
        total_strength = 0
        for instruction in data:
            task = instruction(state)
            while True:
                try:
                    next(task)
                except StopIteration:
                    break
                finally:
                    cycle += 1
                    if (cycle - 20) % 40 == 0:
                        total_strength += state.x * cycle
        return total_strength

    def part2(self, data):
        pass

    # Helpers

    def parse_instruction(self, line):
        line = line.split()
        if line[0] == "noop":
            return noop()
        if line[0] == "addx":
            return addx(int(line[1]))
