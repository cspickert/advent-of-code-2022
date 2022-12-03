import pytest


@pytest.fixture
def example_input():
    return """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


@pytest.fixture
def solution():
    from day01 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day01 as day01_input

    return solution.load_data(day01_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 24000


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 45000


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 67633


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 199628
