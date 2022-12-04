from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        def parse_range(range_str):
            return tuple(map(int, range_str.split("-")))

        def parse_line(line):
            return tuple(map(parse_range, line.split(",")))

        return [parse_line(line) for line in input.splitlines()]

    def part1(self, data):
        return sum(self.either_contains(a, b) for a, b in data)

    def part2(self, data):
        return sum(self.overlaps(a, b) for a, b in data)

    # Helpers

    def either_contains(self, a, b):
        (a1, a2), (b1, b2) = a, b
        return (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2)

    def overlaps(self, a, b):
        (a1, a2), (b1, b2) = a, b
        return self.either_contains(a, b) or (a2 >= b1 and a1 <= b2)
