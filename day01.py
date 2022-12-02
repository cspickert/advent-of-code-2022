from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return (sum(map(int, chunk.splitlines())) for chunk in input.split("\n\n"))

    def part1(self, data):
        return max(data)

    def part2(self, data):
        return sum(sorted(data)[-3:])
