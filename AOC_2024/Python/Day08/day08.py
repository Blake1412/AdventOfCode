from sys import argv
from collections import defaultdict
from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split()

antennas = defaultdict(list)
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col != ".":
            antennas[col].append((i, j))


def get_antinodes(include_self=False, limit_distance=True):
    antinodes = set()

    def add_antinodes(x, y, dx, dy):
        new_x, new_y = (x, y) if include_self else (x + dx, y + dy)
        while 0 <= new_x < len(data) and 0 <= new_y < len(data):
            antinodes.add((new_x, new_y))
            if limit_distance:
                break
            new_x, new_y = new_x + dx, new_y + dy

    for frequency, locations in antennas.items():
        for i in range(len(locations) - 1):
            for j in range(i + 1, len(locations)):
                (x1, y1), (x2, y2) = locations[i], locations[j]
                dx1, dy1, dx2, dy2 = (x1 - x2), (y1 - y2), (x2 - x1), (y2 - y1)
                add_antinodes(x1, y1, dx1, dy1)
                add_antinodes(x2, y2, dx2, dy2)
    return len(antinodes)


def part1():
    return get_antinodes()


def part2():
    return get_antinodes(include_self=True, limit_distance=False)


if __name__ == '__main__':
    timer(part1, part2)
