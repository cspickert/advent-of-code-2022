import pytest


@pytest.fixture
def solution():
    from day06 import Solution

    return Solution()


@pytest.fixture
def real_data(solution):
    from input import day06 as day06_input

    return solution.load_data(day06_input)


def test_example_part1(solution):
    data_1 = solution.load_data("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert solution.part1(data_1) == 7

    data_2 = solution.load_data("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert solution.part1(data_2) == 5

    data_3 = solution.load_data("nppdvjthqldpwncqszvftbrmjlhg")
    assert solution.part1(data_3) == 6

    data_4 = solution.load_data("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert solution.part1(data_4) == 10

    data_5 = solution.load_data("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    assert solution.part1(data_5) == 11


# def test_example_part2(solution, example_data):
#     assert solution.part2(example_data) == 0


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 1757


# def test_part2(solution, real_data):
#     assert solution.part2(real_data) == 0
