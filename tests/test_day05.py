import pytest


@pytest.fixture
def example_input():
    return """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


@pytest.fixture
def solution():
    from day05 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day05 as day05_input

    return solution.load_data(day05_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == "CMZ"


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == "MCD"


def test_part1(solution, real_data):
    assert solution.part1(real_data) == "GFTNRBZPF"


def test_part2(solution, real_data):
    assert solution.part2(real_data) == "VRQWPDSGP"
