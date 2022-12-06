from base import BaseSolution


class Solution(BaseSolution):
    def part1(self, data):
        return self.find_marker(data, 4)

    def part2(self, data):
        return self.find_marker(data, 14)

    # Helper

    def find_marker(self, data, num_chars):
        return next(
            i
            for i in range(num_chars, len(data))
            if len(set(data[i - num_chars : i])) == num_chars
        )
