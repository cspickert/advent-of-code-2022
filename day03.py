import string

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [
            [string.ascii_letters.index(c) + 1 for c in line]
            for line in input.splitlines()
        ]

    def part1(self, data):
        return sum(
            sum(a & b)
            for a, b in [
                (set(values[: len(values) // 2]), set(values[len(values) // 2 :]))
                for values in data
            ]
        )

    def part2(self, data):
        return sum(
            sum(a & b & c)
            for a, b, c in [
                [set(values) for values in data[i : i + 3]]
                for i in range(0, len(data), 3)
            ]
        )
