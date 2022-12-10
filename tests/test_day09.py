import pytest


@pytest.fixture
def example_input():
    return """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


@pytest.fixture
def large_example_input():
    return """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


@pytest.fixture
def solution():
    from day09 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def large_example_data(solution, large_example_input):
    return solution.load_data(large_example_input)


@pytest.fixture
def real_data(solution):
    from input import day09 as day09_input

    return solution.load_data(day09_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 13


def test_small_example_part2(solution, example_data):
    assert solution.part2(example_data) == 1


# def test_large_example_part2(solution, large_example_data):
#     assert solution.part2(large_example_data) == 36


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 6332


# def test_part2(solution, real_data):
#     assert solution.part2(real_data) == 0
