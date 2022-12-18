from unittest.mock import patch

import pytest


@pytest.fixture
def example_input():
    return """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


@pytest.fixture
def solution():
    from day15 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day15 as day15_input

    return solution.load_data(day15_input)


def test_example_part1(solution, example_data):
    with patch.object(solution, "part1_y", 10):
        assert solution.part1(example_data) == 26


# def test_example_part2(solution, example_data):
#     assert solution.part2(example_data) == 0


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 0


# def test_part2(solution, real_data):
#     assert solution.part2(real_data) == 0
