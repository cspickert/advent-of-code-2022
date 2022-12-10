from dataclasses import dataclass

from base import BaseSolution


@dataclass
class State:
    x: int = 1


class Solution(BaseSolution):
    def load_data(self, input):
        return [self.parse_instruction(line) for line in input.splitlines()]

    def part1(self, data):
        state = State()
        cycle = 1
        total_strength = 0
        for instruction in data:
            for _ in instruction(state):
                if (cycle - 20) % 40 == 0:
                    total_strength += state.x * cycle
                cycle += 1
        return total_strength

    def part2(self, data):
        pass

    # Helpers

    def parse_instruction(self, line):
        line = line.split()
        if line[0] == "noop":
            return self.noop()
        if line[0] == "addx":
            return self.addx(int(line[1]))

    def noop(self):
        def fn(state):
            yield

        return fn

    def addx(self, value):
        def fn(state):
            yield
            yield
            state.x += value

        return fn
