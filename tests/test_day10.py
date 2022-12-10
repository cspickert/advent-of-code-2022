import pytest


@pytest.fixture
def example_input():
    return """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


@pytest.fixture
def solution():
    from day10 import Solution

    return Solution()


@pytest.fixture
def example_data(solution, example_input):
    return solution.load_data(example_input)


@pytest.fixture
def real_data(solution):
    from input import day10 as day10_input

    return solution.load_data(day10_input)


def test_example_part1(solution, example_data):
    assert solution.part1(example_data) == 13140


def test_example_part2(solution, example_data):
    assert (
        solution.part2(example_data)
        == """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    )


def test_part1(solution, real_data):
    assert solution.part1(real_data) == 14220


def test_part2(solution, real_data):
    assert (
        solution.part2(real_data)
        == """\
####.###...##..###..#....####.####.#..#.
...#.#..#.#..#.#..#.#....#.......#.#..#.
..#..#..#.#..#.#..#.#....###....#..#..#.
.#...###..####.###..#....#.....#...#..#.
#....#.#..#..#.#.#..#....#....#....#..#.
####.#..#.#..#.#..#.####.#....####..##.."""
    )
