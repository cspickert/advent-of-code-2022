import heapq

from base import BaseSolution


class Solution(BaseSolution):
    START, END = -1, 26

    def load_data(self, input):
        def parse_char(c):
            if c == "S":
                return self.START
            if c == "E":
                return self.END
            return ord(c) - ord("a")

        return [[parse_char(c) for c in line] for line in input.splitlines()]

    def part1(self, data):
        return self.find_shortest_path(data)

    def part2(self, data):
        pass

    # Helpers

    def find_start(self, data):
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == self.START:
                    return row, col

    def find_end(self, data):
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == self.END:
                    return row, col

    def find_shortest_path(self, data):
        start = self.find_start(data)
        end = self.find_end(data)

        if start == end:
            return 0

        heap = [(0, start)]
        seen = {start}

        while heap:
            for _ in range(len(heap)):
                distance, cur_pos = heapq.heappop(heap)
                cur_row, cur_col = cur_pos
                cur_val = data[cur_row][cur_col]

                for next_pos in self.get_adjacent_coords(data, cur_pos):
                    next_row, next_col = next_pos
                    next_val = data[next_row][next_col]

                    if next_val - cur_val > 1:
                        continue

                    if next_pos == end:
                        return distance + 1

                    elif next_pos not in seen:
                        seen.add(next_pos)
                        heapq.heappush(heap, (distance + 1, next_pos))

        return float("inf")

    def get_adjacent_coords(self, data, coords):
        row, col = coords
        result = []
        if row - 1 in range(len(data)):
            result.append((row - 1, col))
        if col - 1 in range(len(data[row])):
            result.append((row, col - 1))
        if row + 1 in range(len(data)):
            result.append((row + 1, col))
        if col + 1 in range(len(data[row])):
            result.append((row, col + 1))
        return result
