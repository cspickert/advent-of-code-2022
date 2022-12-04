import pytest


@pytest.fixture
def example_input():
    return """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


@pytest.fixture
def solution():
    from day04 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day04 as day04_input

    return solution.load_data(day04_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 2


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 4


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 494


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 833
