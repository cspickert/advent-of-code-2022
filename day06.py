from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return input

    def part1(self, data):
        return next(i for i in range(4, len(data)) if len(set(data[i - 4 : i])) == 4)

    def part2(self, data):
        pass
