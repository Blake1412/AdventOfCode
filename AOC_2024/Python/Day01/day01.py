from sys import argv
from collections import defaultdict

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = [line.split() for line in file.read().split("\n")]
    data = (sorted([int(row[0]) for row in data]), sorted([int(row[1]) for row in data]))


def part1():
    sum = 0
    for idx, i in enumerate(data[0]):
        sum += abs(i - data[1][idx])
    return sum


def part2():
    ...
    sum = 0
    frequencies = defaultdict(int)
    for i in data[0]:
        frequencies[i] += 1
    for j in data[1]:
        if j in frequencies:
            sum += j * frequencies[j]
    return sum


if __name__ == '__main__':
    timer(part1, part2)
