from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import List, Optional, Union

from base import BaseSolution


@dataclass
class Directory:
    name: str
    parent: Optional[Directory]
    children: List[Union[File, Directory]] = field(default_factory=list)

    @cached_property
    def size(self):
        return sum(child.size for child in self.children)

    def sum_directory_sizes(self, max_size):
        child_directory_sizes = sum(
            child.sum_directory_sizes(max_size)
            for child in self.children
            if isinstance(child, Directory)
        )
        size = self.size
        if size <= max_size:
            return size + child_directory_sizes
        return child_directory_sizes

    @property
    def descendant_directories(self):
        result = [self]
        for child in self.children:
            if isinstance(child, Directory):
                result.extend(child.descendant_directories)
        return result


@dataclass
class File:
    name: str
    size: int


@dataclass
class State:
    root: Directory
    cwd: Directory


class Solution(BaseSolution):
    def load_data(self, input):
        return self.parse_input(input)

    def part1(self, data):
        return data.sum_directory_sizes(100000)

    def part2(self, data):
        total_space = 70000000
        minimum_space = 30000000
        unused_space = total_space - data.size
        needed_space = minimum_space - unused_space

        dir_sizes = [(d.name, d.size) for d in data.descendant_directories]
        dir_sizes.sort(key=lambda item: item[1])
        for _, size in dir_sizes:
            if size >= needed_space:
                return size

    # Helpers

    def parse_input(self, input):
        lines = input.splitlines()
        state = None
        for line in lines:
            state = self.parse_line(line, state)
        return state.root

    def parse_line(self, line, state):
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    cwd = state.cwd.parent
                elif state is None:
                    root = Directory(line[2], None)
                    return State(root, root)
                else:
                    cwd = next(d for d in state.cwd.children if d.name == line[2])
                return State(state.root, cwd)
        else:
            if line[0] == "dir":
                child = Directory(line[1], state.cwd)
            else:
                child = File(line[1], int(line[0]))
            state.cwd.children.append(child)
        return state
