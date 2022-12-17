import json

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [
            [json.loads(block_line) for block_line in block.splitlines()]
            for block in input.split("\n\n")
        ]

    def part1(self, data):
        return sum(
            i for i, pair in enumerate(data, start=1) if self.is_pair_in_order(pair)
        )

    def part2(self, data):
        pass

    # Helpers

    def is_pair_in_order(self, pair):
        return self.is_pair_in_order_helper(pair) < 0

    def is_pair_in_order_helper(self, pair):
        lhs, rhs = pair
        if isinstance(lhs, int) or isinstance(rhs, int):
            if isinstance(lhs, list):
                return self.is_pair_in_order_helper((lhs, [rhs]))
            if isinstance(rhs, list):
                return self.is_pair_in_order_helper(([lhs], rhs))
            return lhs - rhs
        if len(lhs) > len(rhs):
            return 1
        for lv, rv in zip(lhs, rhs):
            result = self.is_pair_in_order_helper((lv, rv))
            if result != 0:
                return result
        return -1
