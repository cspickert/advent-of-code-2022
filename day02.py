from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [line.split() for line in input.splitlines()]

    def part1(self, data):
        return sum(
            self.get_result(a, b)
            for a, b in (self.parse_match_part1(*pair) for pair in data)
        )

    def part2(self, data):
        return sum(
            self.get_result(a, b)
            for a, b in (self.parse_match_part2(*pair) for pair in data)
        )

    # Helpers

    def parse_move(self, value):
        return "ABC".index(value) + 1

    def parse_match_part1(self, a, b):
        b = b.translate(str.maketrans("XYZ", "ABC"))
        return (self.parse_move(a), self.parse_move(b))

    def parse_match_part2(self, a, b):
        a = self.parse_move(a)
        if b == "X":
            b = {2: 1, 3: 2, 1: 3}[a]
        if b == "Y":
            b = a
        if b == "Z":
            b = {1: 2, 2: 3, 3: 1}[a]
        return (a, b)

    def get_result(self, a, b):
        if a == b:
            return b + 3
        if (a, b) in ((1, 2), (2, 3), (3, 1)):
            return b + 6
        return b
