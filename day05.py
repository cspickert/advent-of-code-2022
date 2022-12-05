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
        return self.get_result(state)

    def part2(self, data):
        state, moves = data
        for move in moves:
            self.do_multi_move(state, move)
        return self.get_result(state)

    # Helpers

    def get_result(self, state):
        return "".join(state[key][0] for key in sorted(state))

    def do_move(self, state, move):
        count, src, dst = move
        count = int(count)
        to_move = state[src][:count]
        state[src] = state[src][count:]
        state[dst] = to_move[::-1] + state[dst]

    def do_multi_move(self, state, move):
        count, src, dst = move
        count = int(count)
        to_move = state[src][:count]
        state[src] = state[src][count:]
        state[dst] = to_move + state[dst]

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
