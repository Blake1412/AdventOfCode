from itertools import product
from sys import argv

from functools import lru_cache

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = list(map(lambda x: [int(x[0]), [int(y) for y in x[1].split()]], [row.split(": ") for row in file.read().split("\n")]))


@lru_cache()
def get_target(value, target, operator):
    if operator == 1 and target > value:
        return target - value
    elif operator == 2 and target % value == 0:
        return target // value
    elif operator == 3:
        target, value = str(target), str(value)
        if target.endswith(value):
            return int(target[:-len(value)] or '0')
    else:
        return None

def is_valid(combination: tuple, values: list, target: int) -> bool:
    val_idx = len(combination)

    while val_idx and target:
        target = get_target(values[val_idx], target, combination[val_idx - 1])
        val_idx -= 1

    return values[0] == target


def part1():
    total = 0
    for left, right in data:
        combinations = product([1, 2], repeat=len(right) - 1)
        for combination in combinations:
            if is_valid(combination, right, left):
                total += left
                break
    return total


def part2():
    total = 0
    for left, right in data:
        combinations = product([1, 2, 3], repeat=len(right) - 1)
        for combination in combinations:
            if is_valid(combination, right, left):
                total += left
                break
    return total


if __name__ == '__main__':
    timer(part1, part2)
