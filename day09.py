from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [
            (direction, int(dist))
            for direction, dist in [line.split() for line in input.splitlines()]
        ]

    def part1(self, data):
        state = (0, 0), (0, 0)
        tails = {state[1]}
        for direction, dist in data:
            for _ in range(dist):
                state = self.move(state, direction)
                tails.add(state[1])
        return len(tails)

    def part2(self, data):
        pass

    # Helpers

    def move(self, state, direction):
        prev_head, tail = state
        (hr, hc) = prev_head
        if direction == "U":
            hr -= 1
        if direction == "L":
            hc -= 1
        if direction == "D":
            hr += 1
        if direction == "R":
            hc += 1
        next_head = (hr, hc)
        if self.should_move_tail(next_head, tail):
            tail = prev_head
        return (next_head, tail)

    def should_move_tail(self, head, tail):
        (hr, hc) = head
        (tr, tc) = tail
        return abs(hr - tr) > 1 or abs(hc - tc) > 1
