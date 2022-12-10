from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [
            (direction, int(dist))
            for direction, dist in [line.split() for line in input.splitlines()]
        ]

    def part1(self, data):
        return self.simulate(data, 2)

    def part2(self, data):
        return self.simulate(data, 10)

    # Helpers

    def simulate(self, data, length):
        state = [(0, 0)] * length
        tails = {state[-1]}
        for direction, dist in data:
            for _ in range(dist):
                state = self.move(state, direction)
                tails.add(state[-1])
        return len(tails)

    def move(self, state, direction):
        state = [*state]

        (hr, hc) = state[0]
        if direction == "U":
            hr -= 1
        if direction == "L":
            hc -= 1
        if direction == "D":
            hr += 1
        if direction == "R":
            hc += 1

        last = state[0]
        state[0] = (hr, hc)

        for i in range(1, len(state)):
            tmp = state[i]
            if self.should_move_tail(state[i - 1], state[i]):
                state[i] = last
            last = tmp

        return state

    def should_move_tail(self, head, tail):
        (hr, hc) = head
        (tr, tc) = tail
        return abs(hr - tr) > 1 or abs(hc - tc) > 1
