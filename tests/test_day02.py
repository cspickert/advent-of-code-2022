import pytest


@pytest.fixture
def example_input():
    return """\
A Y
B X
C Z"""


@pytest.fixture
def solution():
    from day02 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day02 as day02_input

    return solution.load_data(day02_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 15


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 12


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 11063


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 10349
