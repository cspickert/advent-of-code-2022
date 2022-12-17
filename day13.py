import json
import logging
from functools import cmp_to_key

from base import BaseSolution

logger = logging.getLogger(__name__)


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
        data = [item for pair in data for item in pair] + [[[2]], [[6]]]
        data.sort(key=cmp_to_key(lambda a, b: self.is_pair_in_order_helper((a, b))))
        return (1 + data.index([[2]])) * (1 + data.index([[6]]))

    # Helpers

    def is_pair_in_order(self, pair):
        result = self.is_pair_in_order_helper(pair) < 0
        logger.debug(result)
        return result

    def is_pair_in_order_helper(self, pair, indent=0):
        lhs, rhs = pair
        logger.debug(f"{indent * '  '}- Compare {lhs} vs. {rhs}")
        if isinstance(lhs, int) or isinstance(rhs, int):
            if isinstance(lhs, list):
                return self.is_pair_in_order_helper((lhs, [rhs]), indent=indent + 1)
            if isinstance(rhs, list):
                return self.is_pair_in_order_helper(([lhs], rhs), indent=indent + 1)
            return lhs - rhs
        for lv, rv in zip(lhs, rhs):
            result = self.is_pair_in_order_helper((lv, rv), indent=indent + 1)
            if result != 0:
                return result
        if len(lhs) == len(rhs):
            return 0
        if len(lhs) < len(rhs):
            return -1
        return 1
