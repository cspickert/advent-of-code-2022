import re
from collections import defaultdict

from base import BaseSolution


class Solution(BaseSolution):
    part1_y = 2000000

    def load_data(self, input):
        line_re = re.compile(
            r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$"
        )
        return [
            ((sx, sy), (bx, by))
            for sx, sy, bx, by in [
                map(int, line_re.match(line).groups()) for line in input.splitlines()
            ]
        ]

    def part1(self, data):
        grid = defaultdict(int)
        for sensor, beacon in data:
            dist = self.get_distance(sensor, beacon)
            for point in self.get_all_points_within(sensor, dist):
                grid[point] += 1
        beacons = {beacon for _, beacon in data}
        return self.count_coverage(grid, y=self.part1_y, exclude=beacons)

    def part2(self, data):
        pass

    # Helpers

    def count_coverage(self, grid, y, exclude):
        min_x = min(x for x, _ in grid)
        max_x = max(x for x, _ in grid)
        return sum(
            grid[(x, y)] > 0 for x in range(min_x, max_x + 1) if (x, y) not in exclude
        )

    def get_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    def get_all_points_within(self, point, distance):
        point_x, _ = point
        min_x, max_x = point_x - distance, point_x + distance
        for x in range(min_x, max_x + 1):
            other = (x, self.part1_y)
            if self.get_distance(point, other) <= distance:
                yield other

    def print_grid(self, grid, data):
        beacons = {beacon for _, beacon in data}
        sensors = {sensor for sensor, _ in data}

        min_x = min(x for x, _ in grid)
        max_x = max(x for x, _ in grid)
        min_y = min(y for _, y in grid)
        max_y = max(y for _, y in grid)

        for y in range(min_x, max_x + 1):
            print(f"{y:04} ", end="")
            for x in range(min_y, max_y + 1):
                if (x, y) in sensors:
                    print("S", end="")
                elif (x, y) in beacons:
                    print("B", end="")
                elif grid[x, y] > 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
