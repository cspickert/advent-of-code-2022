import pytest


@pytest.fixture
def example_input():
    return """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


@pytest.fixture
def solution():
    from day13 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day13 as day13_input

    return solution.load_data(day13_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 13


def test_example_part2(solution, example_data):
    assert solution.part2(example_data) == 140


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 6420


def test_part2(solution, real_data):
    assert solution.part2(real_data) == 22000
