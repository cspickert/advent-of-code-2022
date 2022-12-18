import pytest


@pytest.fixture
def example_input():
    return """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


@pytest.fixture
def solution():
    from day14 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day14 as day14_input

    return solution.load_data(day14_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 24


# def test_example_part2(solution, example_data):
#     assert solution.part2(example_data) == 0


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 805


# def test_part2(solution, real_data):
#     assert solution.part2(real_data) == 0
