import pytest


@pytest.fixture
def example_input():
    return """\
30373
25512
65332
33549
35390"""


@pytest.fixture
def solution():
    from day08 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day08 as day08_input

    return solution.load_data(day08_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 21


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 8


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 1715


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 374400
