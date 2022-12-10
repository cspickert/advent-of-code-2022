from dataclasses import dataclass, field
from typing import List, Tuple

from base import BaseSolution


@dataclass
class State:
    x: int = 1
    screen_pos: Tuple[int, int] = (0, 0)
    screen: List[str] = field(
        default_factory=lambda: [["." for x in range(40)] for y in range(6)]
    )


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
        state = State()
        for instruction in data:
            for _ in instruction(state):
                self.draw(state)
        return "\n".join("".join(line) for line in state.screen)

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

    def draw(self, state):
        row, col = state.screen_pos
        if col >= len(state.screen[row]):
            col = 0
            row += 1
        if row >= len(state.screen):
            row = 0
        if col in range(state.x - 1, state.x + 2):
            state.screen[row][col] = "#"
        else:
            state.screen[row][col] = "."
        state.screen_pos = (row, col + 1)
