from base import BaseSolution


class Solution(BaseSolution):
    class Abyss(Exception):
        pass

    def load_data(self, input):
        cave = {}
        for line in input.splitlines():
            points = [
                tuple(map(int, reversed(part.split(","))))
                for part in line.split(" -> ")
            ]
            for i in range(len(points) - 1):
                start, end = points[i : i + 2]
                self.trace_line(cave, start, end)

        return cave

    def part1(self, data):
        return self.drop_all_sand(data)

    def part2(self, data):
        pass

    # Helpers

    def drop_all_sand(self, cave):
        try:
            count = 0
            while self.drop_sand(cave):
                count += 1
        except self.Abyss:
            return count

    def drop_sand(self, cave):
        pos = (0, 500)
        self.start_sand(cave, pos)
        final_pos = self.drop_sand_helper(cave, pos)
        return pos != final_pos

    def drop_sand_helper(self, cave, orig_pos):
        pos = orig_pos
        done = False
        while not done:
            next_pos = self.get_next_sand_pos(cave, pos)
            if next_pos == pos:
                self.stop_sand(cave, pos)
                done = True
            else:
                self.move_sand(cave, pos, next_pos)
                pos = next_pos
            if self.is_in_abyss(cave, pos):
                self.stop_sand(cave, pos)
                raise self.Abyss
        return pos

    def get_next_sand_pos(self, cave, pos):
        row, col = pos

        # Try down
        down = (row + 1, col)
        if self.is_valid_sand_pos(cave, down):
            return down

        # Try down-left
        down_left = (row + 1, col - 1)
        if self.is_valid_sand_pos(cave, down_left):
            return down_left

        # Try down-right
        down_right = (row + 1, col + 1)
        if self.is_valid_sand_pos(cave, down_right):
            return down_right

        # Stop
        return pos

    def start_sand(self, cave, pos):
        cave[pos] = "+"

    def move_sand(self, cave, old_pos, new_pos):
        assert cave[old_pos] == "+"
        del cave[old_pos]
        cave[new_pos] = "+"

    def stop_sand(self, cave, pos):
        if self.is_in_abyss(cave, pos):
            del cave[pos]
        else:
            cave[pos] = "o"

    def is_valid_sand_pos(self, cave, pos):
        return pos not in cave

    def is_in_abyss(self, cave, sand):
        max_row = max(pos[0] for pos in cave if cave[pos] == "#")
        min_col = min(pos[1] for pos in cave if cave[pos] == "#")
        max_col = max(pos[1] for pos in cave if cave[pos] == "#")
        return not (
            sand[0] in range(max_row + 1) and sand[1] in range(min_col, max_col + 1)
        )

    def trace_line(self, cave, start, end):
        # Horizontal
        if start[0] == end[0]:
            row = start[0]
            col_min = min(start[1], end[1])
            col_max = max(start[1], end[1])
            for col in range(col_min, col_max + 1):
                cave[row, col] = "#"

        # Vertical
        elif start[1] == end[1]:
            col = start[1]
            row_min = min(start[0], end[0])
            row_max = max(start[0], end[0])
            for row in range(row_min, row_max + 1):
                cave[row, col] = "#"

        # Diagonal
        else:
            raise Exception("diagonal")

    def print_cave(self, cave):
        min_row, max_row = float("inf"), 0
        min_col, max_col = float("inf"), 0

        for (row, col) in cave:
            if row < min_row:
                min_row = row
            if col < min_col:
                min_col = col
            if row > max_row:
                max_row = row
            if col > max_col:
                max_col = col

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                print(cave.get((row, col), "."), end="")
            print()
