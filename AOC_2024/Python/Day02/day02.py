from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = list(map(lambda x: [int(i) for i in x], [row.split() for row in file.read().split("\n")]))


def is_safe(row: list) -> bool:
    increasing, decreasing = 0, 0

    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if not 1 <= abs(diff) <= 3:
            return False
        if diff > 0:
            increasing = 1
        else:
            decreasing = 1
        if increasing and decreasing:
            return False
    return True


def part1():
    safe = 0
    for row in data:
        if is_safe(row):
            safe += 1
    return safe


def part2():
    safe = 0
    for row in data:
        for i in range(len(row)):
            if is_safe(row[0:i] + row[i + 1:len(row)]):
                safe += 1
                break
    return safe


if __name__ == '__main__':
    timer(part1, part2)
