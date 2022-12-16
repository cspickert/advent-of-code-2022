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
        seen = {start}
        return self.find_shortest_path_helper(data, start, end, seen)

    def find_shortest_path_helper(self, data, start, end, seen):
        if start == end:
            return 0

        cur_row, cur_col = start
        cur_val = data[cur_row][cur_col]

        next_moves = []

        for next_pos in self.get_adjacent_coords(data, start):
            if next_pos in seen:
                continue

            next_row, next_col = next_pos
            next_val = data[next_row][next_col]

            if 0 <= (next_val - cur_val) <= 1:
                next_moves.append(next_pos)

        if not next_moves:
            return float("inf")

        return 1 + min(
            self.find_shortest_path_helper(
                data,
                next_pos,
                end,
                {*seen, start},
            )
            for next_pos in next_moves
        )

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
