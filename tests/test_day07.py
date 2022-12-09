import pytest


@pytest.fixture
def example_input():
    return """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@pytest.fixture
def solution():
    from day07 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day07 as day07_input

    return solution.load_data(day07_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 95437


# def test_example_part2(solution, example_data):
#     assert solution.part2(example_data) == 0


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 1232307


# def test_part2(solution, real_data):
#     assert solution.part2(real_data) == 0
