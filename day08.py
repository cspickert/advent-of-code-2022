import operator
from functools import reduce

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [[int(c) for c in line] for line in input.splitlines()]

    def part1(self, data):
        return sum(
            self.is_visible(data, row, col)
            for row in range(len(data))
            for col in range(len(data[row]))
        )

    def part2(self, data):
        return max(
            self.score(data, row, col)
            for row in range(len(data))
            for col in range(len(data[row]))
        )

    # Helpers

    def is_visible(self, grid, row, col):
        return any(
            (
                self.is_visible_top(grid, row, col),
                self.is_visible_left(grid, row, col),
                self.is_visible_bottom(grid, row, col),
                self.is_visible_right(grid, row, col),
            )
        )

    def is_visible_top(self, grid, row, col):
        for y in range(row):
            if grid[y][col] >= grid[row][col]:
                return False
        return True

    def is_visible_left(self, grid, row, col):
        for x in range(col):
            if grid[row][x] >= grid[row][col]:
                return False
        return True

    def is_visible_bottom(self, grid, row, col):
        for y in range(row + 1, len(grid)):
            if grid[y][col] >= grid[row][col]:
                return False
        return True

    def is_visible_right(self, grid, row, col):
        for x in range(col + 1, len(grid[row])):
            if grid[row][x] >= grid[row][col]:
                return False
        return True

    def score(self, grid, row, col):
        return reduce(
            operator.mul,
            (
                self.score_top(grid, row, col),
                self.score_left(grid, row, col),
                self.score_bottom(grid, row, col),
                self.score_right(grid, row, col),
            ),
        )

    def score_top(self, grid, row, col):
        score = 0
        for y in range(row - 1, -1, -1):
            score += 1
            if grid[y][col] >= grid[row][col]:
                break
        return score

    def score_left(self, grid, row, col):
        score = 0
        for x in range(col - 1, -1, -1):
            score += 1
            if grid[row][x] >= grid[row][col]:
                break
        return score

    def score_bottom(self, grid, row, col):
        score = 0
        for y in range(row + 1, len(grid)):
            score += 1
            if grid[y][col] >= grid[row][col]:
                break
        return score

    def score_right(self, grid, row, col):
        score = 0
        for x in range(col + 1, len(grid[row])):
            score += 1
            if grid[row][x] >= grid[row][col]:
                break
        return score
