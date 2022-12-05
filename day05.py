from collections import defaultdict

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        diagram, instructions = input.split("\n\n")
        return self.parse_diagram(diagram), self.parse_instructions(instructions)

    def part1(self, data):
        state, moves = data
        for move in moves:
            self.do_move(state, move)
        return "".join(state[key][0] for key in sorted(state))

    def part2(self, data):
        pass

    # Helpers

    def do_move(self, state, move):
        count, src, dst = move
        for _ in range(int(count)):
            state[dst].insert(0, state[src].pop(0))

    def parse_diagram(self, diagram_str):
        *stacks, keys = [
            [line[i : i + 4][1] for i in range(0, len(line), 4)]
            for line in diagram_str.splitlines()
        ]
        result = defaultdict(list)
        for i, key in enumerate(keys):
            for stack in stacks:
                if i < len(stack) and stack[i] != " ":
                    result[key].append(stack[i])
        return result

    def parse_instructions(self, instructions_str):
        return [
            (item[1], item[3], item[5])
            for item in [line.split() for line in instructions_str.splitlines()]
        ]
