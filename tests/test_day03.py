import pytest


@pytest.fixture
def example_input():
    return """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


@pytest.fixture
def solution():
    from day03 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day03 as day03_input

    return solution.load_data(day03_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 157


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 70


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 7674


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 2805
